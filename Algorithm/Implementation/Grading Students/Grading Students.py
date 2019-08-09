#!/bin/python3

import os
import sys

def gradingStudents(grades):
    res = []
    for i in grades:
        mul_five = i//10*10
        while mul_five < i:
            mul_five += 5
        if mul_five >=40 and abs(mul_five-i) <3:
            res.append(mul_five)
        else:
            res.append(i)
    return res

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
