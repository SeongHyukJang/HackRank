#!/bin/python3

import math
import os
import random
import re
import sys

def LeapYearForJulian(year):
    if year%4 == 0:
        return True
    else:
        return False

def LeapYearForGregorian(year):
    if year%400 == 0:
        return True
    if year%4 == 0:
        if year%100 != 0:
            return True
    else:
        return False

def dayOfProgrammer(year):
    if year > 1918:
        if LeapYearForGregorian(year):
            return "12.09." + str(year)
        else:
            return "13.09." + str(year)
    elif year == 1918:
        return "26.09.1918"
        
    else:
        if LeapYearForJulian(year):
            return "12.09." + str(year)
        else:
            return "13.09." + str(year)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
