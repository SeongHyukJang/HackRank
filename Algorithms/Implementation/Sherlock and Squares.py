#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):            
    min_num = int(math.sqrt(a)+1)
    max_num = int(math.sqrt(b)+1)
    
    if math.sqrt(a) == int(math.sqrt(a)):
        return max_num - min_num + 1
    
    return max_num - min_num
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
