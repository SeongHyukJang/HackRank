# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
K,M = map(int,input().split())
counter = 0

mylist = []
while counter != K:
    elements = list(map(int,input().split()))
    elements.remove(elements[0])
    mylist.append(list(map(lambda y: pow(y,2),elements)))
    counter +=1
if len(mylist) != 1:
    temp = mylist[0]
    for i in range(1,len(mylist)):
        x = list(set(list(itertools.product(temp,mylist[i]))))
        y = set(map(lambda y:sum(y),x))
        temp = y

else:
    y = mylist[0]

print(max(set(map(lambda z: z%M ,y))))
