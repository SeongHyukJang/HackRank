#!/bin/python3

import os
import sys

def getTotalX(a, b):
    res = 0
    c = a+b
    start = max(a)
    end = min(b)
    for i in range(start, end+1):
        counter = 0
        for j in a:
            if i%j == 0:
                counter += 1
        for k in b:
            if k%i == 0:
                counter += 1
        if counter == len(c):
            res += 1
    return res

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
