#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    if len(s) % 2 == 1:
        return -1
    
    buff = dict()
    for i in range(int(len(s)/2)):
        if s[i] not in buff.keys():
            buff[s[i]] = 1
        else:
            buff[s[i]] += 1
    
    res = 0
    for key in buff.keys():
        word = s[int(len(s)/2):]
        if buff[key] > word.count(key):
            res += (buff[key] - word.count(key))
            
    return res
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
