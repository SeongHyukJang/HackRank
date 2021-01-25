#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    buff = dict()
    for letter in s1:
        if letter not in buff.keys():
            buff[letter] = 1
        else:
            buff[letter] += 1
    
    res = len(s1) + len(s2)
    for key in buff.keys():
        if key in s2:
            res -= min(buff[key], s2.count(key))*2
                
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
