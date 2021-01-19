#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    num = 0
    
    for number in range(p,q+1):
        squared = number*number
        
        r = str(squared)[-len(str(number)):]
        l = str(squared)[:len(str(squared))-len(r)]
        if l == '':
            l = 0
        
        if int(l) + int(r) == number:
            num += 1
            print(number,end = ' ')
            
    if num == 0:
        print("INVALID RANGE")
        

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
