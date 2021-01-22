#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    min_i = 0; min_j = 0
    max_i = len(grid)-1; max_j = len(grid[0])-1
    
    res = []
    for i in range(len(grid)):
        row = ""
        for j in range(len(grid[i])):
            if i > min_i and i < max_i:
                if j > min_j and j < max_j:
                    left_cell = int(grid[i][j-1])
                    right_cell = int(grid[i][j+1])
                    top_cell = int(grid[i-1][j])
                    bottom_cell = int(grid[i+1][j])
                    
                    if int(grid[i][j]) > max(left_cell, right_cell, top_cell, bottom_cell):
                        row += 'X'
                        continue
            row += grid[i][j]
        res.append(row)
                
    return res
            
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
