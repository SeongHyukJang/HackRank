import numpy as np

lst = list(map(int,input().split()))
res = np.array(lst).reshape(3,3)
print(res)