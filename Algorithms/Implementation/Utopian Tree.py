#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
buff = [1]
def utopianTree(n):
    res = 1
    
    if n+1 > len(buff):
        for i in range(len(buff), n+1):
            if i%2 == 0:
                buff.append(buff[i-1] + 1)
            else:
                buff.append(buff[i-1] * 2)
    return buff[n]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
