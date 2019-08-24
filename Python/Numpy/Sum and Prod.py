import numpy as np

N,M = map(int, input().split())

lst = [input().split() for _ in range(N)]
arr = np.array(lst, int)

S = np.sum(arr, axis = 0)
P = np.product(S)

print(P)