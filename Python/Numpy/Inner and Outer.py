import numpy as np

lst1 = [input().split()]
lst2 = list(map(int, input().split()))

arr1 = np.array(lst1, int)
arr2 = np.array(lst2, int)

print(int(np.inner(arr1,arr2)), np.outer(arr1, arr2), sep = '\n')