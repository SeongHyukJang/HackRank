ElmentsM = int(input())
M = set(map(int,input().split(" ")))
ElementsN = int(input())
N = set(map(int,input().split(" ")))
res = (M-N).union(N-M)
res = sorted(list(res))
for i in res:
    print(i)
