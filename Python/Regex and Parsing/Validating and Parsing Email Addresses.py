import re, email.utils

n = int(input())
pattern = r'[a-zA-Z]([\w\.-]*)@([a-zA-Z]*)\.([a-zA-Z]{1,3})'
for i in range(n):
    string = input()
    res = email.utils.parseaddr(string)
    match = re.match(pattern,res[1])
    if match != None:
        if match.group() == res[1]:
            print(email.utils.formataddr(res))