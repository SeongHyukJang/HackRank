import re
pattern = r'([0-9a-zA-Z])\1+'
string = input()

x = re.search(pattern,string)
if x == None:
    print(-1)
else:
    print(x.group(1))
