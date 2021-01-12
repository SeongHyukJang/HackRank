#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    if n == 1:
        print(1)
    else:
        res = 1
        for i in range(1,n+1):
            res *= i
        print(res)
    
    
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
