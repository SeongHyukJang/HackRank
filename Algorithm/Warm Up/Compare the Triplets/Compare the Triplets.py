#!/bin/python3

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    a_point = 0
    b_point = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            a_point += 1
        elif a[i] < b[i]:
            b_point += 1
    return [a_point, b_point]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
