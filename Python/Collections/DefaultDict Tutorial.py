# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m = map(int,input().split())

x = defaultdict(list)
for i in range(n):
    x[input()].append(i+1)

B = []
for i in range(m):
    B.append(input())

for i in B:
    if i in x:
        print(' '.join(map(str,x[i])))
    else:
        print(-1)      
