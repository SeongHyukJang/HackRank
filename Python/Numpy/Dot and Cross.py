import numpy as np

N = int(input())

lst1 = [input().split() for _ in range(N)]
lst2 = [input().split() for _ in range(N)]

arr1 = np.array(lst1, int)
arr2 = np.array(lst2, int)

print(np.dot(arr1,arr2))