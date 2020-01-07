#!/bin/python3

import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    ActualBill = 0
    for i in range(len(bill)):
        if i != k:
            ActualBill += bill[i]
    ActualBill /= 2
    if ActualBill == b:
        print("Bon Appetit")
    else:
        print(int(b - ActualBill))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
