# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
N = int(input())
mylist = input().split()
K = int(input())
x = list(itertools.combinations(mylist,K))
counter = 0
for i in x:
    if 'a' in i:
        counter +=1
print(format(counter/len(x),'.3f'))
