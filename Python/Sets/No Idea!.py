# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = input().split(' ')
array = list(input().split(' '))
A = set(input().split(' '))
B = set(input().split(' '))
res = 0

for i in array:
    if i in A:
        res += 1
    elif i in B:
        res -= 1
print(res)
