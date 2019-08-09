#!/bin/python3

import os
import sys

def timeConversion(s):
    #
    # Write your code here.
    #
    ele_list = s.split(":")
    if ele_list[2].endswith("PM"):
        ele_list[0] = str(int(ele_list[0]) + 12)
    if ele_list[0] == "24":
        ele_list[0] = "12"
    if ele_list[0] == "12" and ele_list[2].endswith("AM"):
        ele_list[0] = "00"
    ele_list[2] = ele_list[2][:2]
    return ":".join(ele_list)
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
