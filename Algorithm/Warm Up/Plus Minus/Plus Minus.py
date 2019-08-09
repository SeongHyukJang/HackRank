#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(arr):
    PlusCount = 0
    MinusCount = 0
    ZeroCount = 0
    for i in arr:
        if i > 0:
            PlusCount += 1
        elif i < 0:
            MinusCount += 1
        else:
            ZeroCount += 1
    print(format(PlusCount/n,".6f"))
    print(format(MinusCount/n,".6f"))
    print(format(ZeroCount/n,".6f"))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
