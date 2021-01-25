#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    if len(s) == 1:
        print("NO")
        return
    idx = 0
    count = 1
    begin_num = s[idx:idx+count]
    num = begin_num
    next_num = -1

    start_count = count
    temp = 1
    checking = False
    while True:
        next_num = s[idx+1:idx+count+temp]
        if int(next_num) - int(num) != 1:
            temp += 1
            if idx+count+temp-1 > len(s):
                start_count += 1
                if idx+start_count >= len(s):
                    if checking:
                        idx = 0
                        checking = False
                    else:
                        print("NO")
                        return
                count = start_count
                num = s[0:count]
                begin_num = num
                idx = count-1
                temp = 1
        else:
            num = next_num
            idx += (count+temp-1)
            temp = 1
            if idx >= len(s)-1:
                break

    if begin_num[0] == '0':
        print("NO")
        return
    print("YES",begin_num)

    
    

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
