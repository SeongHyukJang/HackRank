import numpy as np

N,M,P = map(int,input().split())

lst1 = []
for i in range(N):
    lst1.append(list(map(int,input().split())))

lst2 = []
for i in range(M):
    lst2.append(list(map(int,input().split())))

lst1 = np.array(lst1)
lst2 = np.array(lst2)

print(np.concatenate((lst1,lst2)))