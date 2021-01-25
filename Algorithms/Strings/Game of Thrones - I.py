#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    buff = []
    for letter in set(s):
        if s.count(letter) % 2 == 1:
            buff.append(letter)
            
    if len(buff) != 0:
        if len(s) % 2 == 1 and len(buff) == 1:
            return "YES"
        else:
            return "NO"
        
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
