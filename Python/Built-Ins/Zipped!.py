# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X = map(int,input().split())

data = []
for i in range(X):
    data.append(list(map(float,input().split())))

Sum = list(zip(*data))
for i in range(N):
    print(format(sum(Sum[i])/X,"0.1f"))
