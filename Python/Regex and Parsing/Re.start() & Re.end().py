import re
string = input()
tofind = input()

pattern = r'' + tofind[:-1] + '(?=' + tofind[-1] +')'


if tofind not in string:
    print((-1,-1))

matches = re.finditer(pattern,string)
for match in matches:
    print((match.start(),match.end()))