#!/bin/python3

import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    res_count = arr.count(1)
    res = 1
    for i in range(2,6):
        if  arr.count(i) >= res_count:
            if res_count == arr.count(i):
                res = min(res,i)
            else:
                res = i
            res_count = arr.count(i)

    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
