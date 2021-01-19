#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    res = 0
    page = 1
    for problems in arr:
        number = [i+1 for i in range(problems)]
        count = 0
        for num in number:
            count += 1
            if num == page:
                res += 1
                
            if count == k:
                count = 0
                page += 1
        if count != 0:
            page += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
