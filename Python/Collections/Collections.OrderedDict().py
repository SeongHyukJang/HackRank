# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict,Counter
res = OrderedDict()
num = int(input())

counter = 0
while counter != num:
    item_name = ''
    elements = input().split()
    net_price = int(elements[-1])
    if len(elements) >2:
        for i in elements[:-1]:
            item_name += ' ' + i 
        item_name = str(item_name).lstrip(' ')
        if item_name in res:
            res[item_name] += net_price
        else:
            res[item_name] = net_price
    else:
        item_name = str(elements[0])
        if item_name in res:
            res[item_name] += net_price
        else:
            res[item_name] = net_price
    counter+=1
for i in res:
    res[i] = str(res[i])
for i in res.items():
    print(' '.join(i))
