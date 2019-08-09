# Enter your code here. Read input from STDIN. Print output to STDOUT
x,k = map(int,input().split())
check = input()
res = eval(check)

if(res == k):
    print(True)
else:
    print(False)
