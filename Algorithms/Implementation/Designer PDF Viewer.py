#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    buff = dict()
    idx = 0
    for height in h:
        buff[alphabet[idx]] = height
        idx += 1
    
    highest = 1
    
    for letter in word:
        if buff[letter] > highest:
            highest = buff[letter]
    
    return len(word) * highest
    
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
