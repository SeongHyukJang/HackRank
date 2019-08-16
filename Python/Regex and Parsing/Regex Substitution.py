import re

string = ''
n = int(input())
for i in range(n):
    line = input()
    res1 = re.sub(r'(\s)(&&)(?=\s)', ' and',line)
    res2 = re.sub(r'(\s)(\|\|)(?=\s)', ' or', res1)
    string += res2
    string += '\n'

print(string)