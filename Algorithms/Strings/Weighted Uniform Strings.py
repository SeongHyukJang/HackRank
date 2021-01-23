#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    res = []
    w = '_abcdefghijklmnopqrstuvwxyz'
    
    possible_weights = []
    idx = 0
    while idx < len(s):
        letter = s[idx]
        
        count = 1
        possible_weights.append(w.find(letter)*count)
        while idx+count < len(s) and letter == s[idx+count]:
            count += 1
            possible_weights.append(w.find(letter)*count)
        
        idx += count
           
    possible_weights = set(possible_weights)
    for q in queries:
        if q in possible_weights:
            res.append("Yes")
        else:
            res.append("No")
            
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
