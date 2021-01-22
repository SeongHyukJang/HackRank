#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    
    buff = dict()
    
    for idx in range(len(b)):
        if b[idx] not in buff:
            buff[b[idx]] = [idx]
        else:
            buff[b[idx]].append(idx)
        
    can_move = False
    if '_' in buff.keys():
        can_move = True
        
    for letter in buff.keys():
        if letter != '_' and len(buff[letter])== 1:
            return "NO"
        else:
            temp = buff[letter]
            for i in range(len(temp)-1):
                if temp[i+1] - temp[i] != 1:
                    if not can_move:
                        return "NO"
    
    return "YES"
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
