#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    
    buff = []
    for person in B:
        if person % 2 != 0:
            buff.append(1)
        else:
            buff.append(0)
            
    res = 0
    while 1 in buff:
        idx = 0
        while buff[idx] == 0:
            idx+=1
        if idx+1 >= len(buff):
            return "NO"
        if buff[idx] == 1:
            if buff[idx+1] == 1:
                buff[idx+1] = 0
            else:
                buff[idx+1] = 1
            buff[idx] = 0
            res += 2
        
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
