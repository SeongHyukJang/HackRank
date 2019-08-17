#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

string = ''
for i in zip(*matrix):
    string += ''.join(i)
# r'(?<=[\w\s])([^A-Za-z0-9]+)(?=[\w\s])
temp = re.sub(r'(?<=[\w])([^\w]+)(?=[\w])',' ', string)
res = re.sub(r'\s\s',' ',temp)
print(res)
