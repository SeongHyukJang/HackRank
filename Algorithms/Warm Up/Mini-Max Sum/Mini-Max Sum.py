#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    res = []
    val = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                for p in range(k+1,len(arr)):
                    val += (arr[i]+arr[j]+arr[k]+arr[p])
                    res.append(val)
                    val = 0
    print(min(res),max(res))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
