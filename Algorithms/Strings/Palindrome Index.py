#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    reverse_s = s[::-1]
    if s == reverse_s:
        return -1
    res = 0
    for i in range(len(s)):
        if s[i] != reverse_s[i]:
            temp_s = s[0:i]
            temp_s += s[i+1:]
            
            if temp_s == temp_s[::-1]:
                return i
            else:
                return len(s)-i-1
            
    return -1
            
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
