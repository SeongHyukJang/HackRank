#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    res = ''
    answer = 'hackerrank'
    for letter in s:
        if letter == answer[0]:
            res += letter
            answer = answer[1:]
        if len(answer) == 0:
            break
        
    if res == 'hackerrank':
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
