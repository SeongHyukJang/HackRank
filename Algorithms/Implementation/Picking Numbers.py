#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    buff = dict()
    for elem in a:
        if elem in buff:
            buff[elem] += 1
        else:
            buff[elem] = 1

    res = -1
    for elem in buff.keys():
        if elem-1 in buff.keys():
            tmp = buff[elem] + buff[elem-1]
            if tmp > res:
                res = tmp
        if elem+1 in buff.keys():
            tmp = buff[elem] + buff[elem+1]
            if tmp > res:
                res = tmp
        if buff[elem] > res:
            res = buff[elem]
    return res
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
