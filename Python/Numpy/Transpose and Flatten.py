import numpy as np

n,m = map(int,input().split())

lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))

arr = np.array(lst)
print(arr.transpose())
print(arr.flatten())