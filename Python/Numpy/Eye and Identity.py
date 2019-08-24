import numpy as np

N,M = map(int,input().split())

res = np.eye(N,M)
res = str(res).replace('1.',' 1.')
res = res.replace('0.',' 0.')

print(res)