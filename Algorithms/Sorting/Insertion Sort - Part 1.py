#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    idx = len(arr)-1
    temp = arr[idx]
    while True:
        if idx == 0:
            arr[idx] = temp
            for elem in arr:
                print(elem, end=' ')
            return
        if arr[idx-1] > temp:
            arr[idx] = arr[idx-1]
            for elem in arr:
                print(elem, end=' ')
            print()
        else:
            arr[idx] = temp
            for elem in arr:
                print(elem, end = ' ')
            print()
            return
        idx -= 1

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
    
