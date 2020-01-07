#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    up_result = 0
    down_result = 0
    res = [scores[0]]
    for i in range(1,len(scores)):
        if scores[i] > max(res):
            up_result += 1
        elif scores[i] < min(res):
            down_result += 1
        res.append(scores[i])
    return [up_result, down_result]




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
