#!/bin/python3

import os
import sys

def pageCount(n, p):
    res = 0
    BookPages = []
    page = 0
    while page < n+1:
        BookPages.append((page,page+1))
        page += 2
    for i in range(len(BookPages)):
        if p in BookPages[i]:
           res = i
    BookPages.reverse()
    for i in range(len(BookPages)):
        if p in BookPages[i]:
            if i < res:
                res = i 
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
