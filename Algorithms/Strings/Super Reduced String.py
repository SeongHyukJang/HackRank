#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    CountList = list(set(s))
    while True:
        for letter in CountList:
            while letter + letter in s:
                x = s.index(letter+letter)
                s = s[:x] + s[x+2:]
        counter = 0
        for letter in CountList:
            if letter + letter not in s:
                counter += 1
        if counter == len(CountList):
            break
    if s == "":
        return "Empty String"
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
