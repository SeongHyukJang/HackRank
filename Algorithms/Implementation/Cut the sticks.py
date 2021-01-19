#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    res = [len(arr)]
    
    while len(arr) != 0:
        shortest = min(arr)
        count = 0
        while shortest in arr:
            arr.remove(shortest)    
            count += 1
        res.append(res[-1]-count)
    res.remove(0)
    return res
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
