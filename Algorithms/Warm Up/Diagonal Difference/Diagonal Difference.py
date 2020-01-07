#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    LtoRdiagonal = 0
    RtoLdiagonal = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                LtoRdiagonal += arr[i][j]
            if abs(i+j) == n-1:
                RtoLdiagonal += arr[i][j]
    return abs(LtoRdiagonal - RtoLdiagonal)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
