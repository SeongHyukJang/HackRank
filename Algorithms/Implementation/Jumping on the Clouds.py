#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    length = len(c)
    
    count = 0
    idx = 0
    while idx != length-1:
        if idx + 2 == length-1:
            idx += 2
            count += 1
            break
        elif idx + 1 == length-1:
            idx += 1
            count += 1
            break
        
            
        if c[idx+2] != 1:
            idx += 2
            count += 1
        elif c[idx+1] != 1:
            idx += 1
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
