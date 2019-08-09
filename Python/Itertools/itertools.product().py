# Enter your code here. Read input from STDIN. Print output to STDOUT
A = sorted(map(int,input().split()))
B = sorted(map(int,input().split()))
from itertools import product

x = list(product(A,B))
for i in x:
    print(i,end = ' ')
