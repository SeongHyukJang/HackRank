#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    
    elements = set(arr)
    countElem = dict()
    
    for elem in elements:
        countElem[elem] = arr.count(elem)
    
    count = 0
    while len(countElem) != 1:
        discardElem = -1
        for elem in countElem.keys():
            if min(countElem.values()) == countElem[elem]:
                discardElem = elem
                break
                
        while discardElem in arr:
            arr.remove(discardElem)
            count += 1
        countElem.pop(discardElem)
    return count
        
    
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
