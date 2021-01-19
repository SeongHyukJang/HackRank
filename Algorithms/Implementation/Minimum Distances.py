#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    buff = dict()
    
    for idx in range(len(a)):
        if a[idx] not in buff.keys():
            buff[a[idx]] = [idx]
        else:
            buff[a[idx]].append(idx)
    
    res = -1
    for key in buff.keys():
        if len(buff[key]) == 2:
            temp = buff[key][1] - buff[key][0]
            if res == -1:
                res = temp
            elif temp < res:
                res = temp
    
    return res
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
