#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    res = 0
    while len(s) != 0:
        temp = s[0:3]
        if temp[0] != 'S':
            res += 1
        if temp[1] != 'O':
            res += 1
        if temp[2] != 'S':
            res += 1

        s = s[3:]
        
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
