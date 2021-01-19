#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    cities = [0]*n
    
    for city in c:
        cities[city] = 1
        
    res = [0]
    c.sort()
    for idx in range(len(cities)):
        if cities[idx] == 0:


            start = 0
            end = len(c)-1
            mid = -1
            while start <= end:    
                mid = int((start+end)/2)
                if c[mid] == idx:
                    break
                elif c[mid] > idx:
                    end = mid-1
                else:
                    start = mid+1
            if start < 0:
                start = 0
            elif start >= len(c):
                start = len(c)-1
            if end < 0:
                end = 0
            elif end >= len(c):
                end = len(c)-1
            res.append(min(abs(idx - c[start]),abs(c[end] - idx)))

    return max(res)
            
                        
                    
                        
            
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
