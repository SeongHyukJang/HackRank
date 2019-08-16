import re
n = int(input())
pattern = r'^(7|8|9)\d{9}$'

for i in range(n):
    string = input()
    res = re.match(pattern,string)
    if res:
        print("YES")
    else:
        print("NO")