import re
pattern = r'#([\dABCDEF]{6}|[\dABCDEF]{3})'

n = int(input())
s = ''
for i in range(n):
    string = input()
    if "{" in string and "#" not in string:
        s = "{"
    elif "}" in string:
        s = ""
    if s == "{":
        match = re.finditer(pattern,string,re.I)
        if match != None:
            for i in match:
                print(i.group())