#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    beautiful = 0
    for day in range(i, j+1):
        tmp = day
        reverse = 0
        
        buff = []
        while tmp > 0:
            buff.append(int(tmp%10))
            tmp = int(tmp/10)
        
        res = 0;n=1;idx=len(buff)-1
        
        while idx >= 0:
            res += (buff[idx] * n)
            n *= 10
            idx -= 1
            
        if abs(res-day) % k == 0:
            beautiful += 1
        
    return beautiful
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
