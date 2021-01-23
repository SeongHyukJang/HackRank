#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    res = 0
    
    idx = 0
    while idx < len(s):
        char = s[idx]
        count = 0
        while idx + count < len(s) and s[idx+count] == char:
            count += 1
            
        res += (count-1)    
        idx += count
        
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
