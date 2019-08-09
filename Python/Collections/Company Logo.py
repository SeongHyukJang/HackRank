#!/bin/python3

import math
import os
import random
import re
import sys
import collections


if __name__ == '__main__':
    s = input()
s1 = ''.join(sorted(s))
s2 = collections.Counter(s1)

elements = collections.Counter(s2)
res = elements.most_common()
count = 0
for i in res:
    if count == 3:
        break
    print(i[0],i[1])
    count += 1
