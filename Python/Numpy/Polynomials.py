import numpy as np

P = list(map(float,input().split()))
x = int(input())


print(np.polyval(P,x))