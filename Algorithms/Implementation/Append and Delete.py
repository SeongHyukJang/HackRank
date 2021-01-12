#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    if s == t:
        return "Yes"
    
    idx = 0
    while s[idx] == t[idx]:
        idx += 1
        if idx == len(s) or idx == len(t):
            break
    
    remain_char_s = len(s) - idx
    remain_char_t = len(t) - idx
    
    remove_all = k - len(s)
    if remove_all >= len(t):
        return "Yes"
        
    remain = k - remain_char_s
    if remain - remain_char_t >= 0:
        if (remain - remain_char_t) % 2 == 0:
            return "Yes"
    return "No"
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
