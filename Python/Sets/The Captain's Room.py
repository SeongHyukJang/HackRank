# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
n = int(input())
x = collections.Counter(input().split())
for i in x:
    if x[i] != n:
        print(i)
