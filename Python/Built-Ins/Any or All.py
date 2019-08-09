# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
data = list(map(int,input().split()))
print( all( [all(map(lambda x: x>0, data)) , any(map(lambda x:x == int(str(abs(x))[::-1]),data)) ] ) )

#Another solution
'''
i = 0
res = False
while i != N:
    if data[i] <0:
        res &= False
    if data[i] >0:
        if data[i] == int(str(data[i])[::-1]):
            res |= True
    i += 1
print(res)
'''
