import numpy as np

N = int(input())

lst = [input().split() for _ in range(N)]

arr = np.array(lst, float)

res = round(np.linalg.det(arr),2)
print(res)