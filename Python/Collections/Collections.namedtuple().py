# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
num = int(input())
Slist = namedtuple('Slist',input().split())

counter = 0
res = 0
while counter != num:
    elements = input().split()
    ele1 = Slist(elements[0],elements[1],elements[2],elements[3])
    res += int(ele1.MARKS)
    counter += 1

print(format(res/num,'.2f'))
