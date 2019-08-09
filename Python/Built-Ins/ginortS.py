# Enter your code here. Read input from STDIN. Print output to STDOUT

s = sorted(input())

lower = ''
upper = ''
odd = ''
even = ''

for i in s:
    if(i.islower()):
        lower += i
    
    if(i.isupper()):
        upper += i
    
    if(i.isdigit()):
        if int(i)%2 == 0:
            even += i

        else:
            odd += i

res = lower + upper + odd + even
print(res)
