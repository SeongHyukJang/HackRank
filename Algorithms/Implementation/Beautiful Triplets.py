#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    res = 0
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] - arr[i] == d:
                for k in range(j+1, len(arr)):
                    if arr[k] - arr[j] == d:
                        res += 1
                    elif arr[k] - arr[j] > d:
                        break
            elif arr[j] - arr[i] > d:
                break        
            
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
