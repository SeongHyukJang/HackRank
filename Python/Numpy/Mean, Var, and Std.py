import numpy as np
np.set_printoptions(legacy = '1.13')
N,M = map(int,input().split())

lst = [input().split() for _ in range(N)]

arr = np.array(lst, int)

mean = np.mean(arr, axis = 1)
var = np.var(arr, axis = 0)
std = np.std(arr)

print(mean, var, std, sep = '\n')