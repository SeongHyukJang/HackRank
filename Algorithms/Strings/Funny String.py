#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    ord_diff = []
    
    for i in range(len(s)-1):
        val = abs(ord(s[i+1]) - ord(s[i]))
        ord_diff.append(val)

    if ord_diff == ord_diff[::-1]:
        return "Funny"
    return "Not Funny"
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
