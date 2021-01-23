#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
                    
    res = ''
    
    for letter in s:
        isupper = letter.isupper()
        idx = alphabet.find(letter.lower())
        
        if idx != -1:
            idx += k
            idx %= len(alphabet)
            if isupper:
                res += alphabet[idx].upper()
            else:
                res += alphabet[idx]
        else:
            res += letter
        
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
