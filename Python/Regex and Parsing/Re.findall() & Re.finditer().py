import re

vowel = "aeiouAEIOU"
s = input()
pattern = r'(?<=[^%s])([%s]{2,})(?=[^%s])' %(vowel,vowel,vowel)


check = re.search(pattern,s)
if check == None:
    print(-1)

res = re.finditer(pattern,s)
for i in res:
    print(i.group())
