import numpy as np

N,M = map(int,input().split())

lst = [input().split() for _ in range(N)]

arr = np.array(lst,int)

Min = np.min(arr, axis = 1)
Max = np.max(Min)
print(Max)