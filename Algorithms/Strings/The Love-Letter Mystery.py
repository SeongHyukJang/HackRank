#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    reverse_s = s[::-1]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    res = 0
    for i in range(int(len(reverse_s)/2)):
        if alphabet.find(reverse_s[i]) >= alphabet.find(s[i]):
            idx = alphabet.find(reverse_s[i])
            target = s[i]
        else:
            idx = alphabet.find(s[i])
            target = reverse_s[i]
        count = 0
        while alphabet[idx] != target:
            idx -= 1
            count += 1
        
        res += count
    return res
            
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
