#!/bin/python3

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    AppleCount = 0
    OrangeCount = 0
    for i in range(len(apples)):
        apples[i] += a
    for elements in apples:
        if elements>=s and elements<=t:
            AppleCount +=1 
    for i in range(len(oranges)):
        oranges[i] += b
    for elements in oranges:
        if elements >=s and elements <= t:
            OrangeCount += 1
    print(AppleCount)
    print(OrangeCount)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
