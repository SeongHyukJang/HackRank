# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s,k = input().split()
k = int(k)
s = sorted(list(s))
res = combinations_with_replacement(s,k)
for i in res:
    counter = 0
    ele = ''
    while counter != k:
        ele += i[counter]
        counter += 1
    print(ele)
