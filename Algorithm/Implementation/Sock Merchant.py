#!/bin/python3

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    counter = 0
    for i in set(ar):
         if ar.count(i) >= 2:
             counter += int(ar.count(i)/2)
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
