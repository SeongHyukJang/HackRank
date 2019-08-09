# Enter your code here. Read input from STDIN. Print output to STDOUT
s ,k = input().split()
k = int(k)
from itertools import permutations
res = list(permutations(s,k))
res.sort()

for i in res:
    counter = 0
    ele = ''
    while counter != k:
        ele += i[counter]
        counter +=1
    print(ele)
