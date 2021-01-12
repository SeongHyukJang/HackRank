#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    buff = dict()
    res = [-1 for _ in range(len(p))]
    
    index = 1
    for number in p:
        buff[number] = index
        res[number-1] = index
        index += 1

        
    for i in range(len(res)):
        res[i] = buff[res[i]]
        
    return res
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
