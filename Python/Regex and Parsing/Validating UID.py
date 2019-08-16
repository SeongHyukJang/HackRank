import re
pattern = r'[\w^_]'

for i in range(int(input())):
    matches = re.finditer(pattern,input())
    check = ''
    for match in matches:
        if match.group() not in check:
            check += match.group()

    upper = 0
    digit = 0
    for i in check:
        if i.isupper():
            upper += 1
        elif i.isdigit():
            digit += 1
    if upper >= 2 and digit >=3 and len(check) == 10 :
        print("Valid")
    else:
        print("Invalid")