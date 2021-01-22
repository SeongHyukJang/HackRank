#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    
    letters = list(set(s))
    
    res = [0]
    
    for i in range(len(letters)):
        for j in range(i+1, len(letters)):
            char1 = letters[i]; char2 = letters[j]
            
            temp = s
            for letter in temp:
                if letter != char1 and letter != char2:
                    temp = temp.replace(letter,'')
            
            checker = False
            for idx in range(len(temp)-1):
                if temp[idx] == temp[idx+1]:
                    checker = True
                    break
                
            if not checker:
                res.append(len(temp))
                
    return max(res) 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
