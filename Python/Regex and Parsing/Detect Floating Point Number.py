import re
pattern = re.compile('[+-.]?[0-9]*\.[0-9]+')

n = int(input())
for i in range(n):
    string = input()
    match = pattern.fullmatch(string)
    if match != None:
        print(True)
    else:
        print(False)

'''
n = int(input())

for i in range(n):
    s = input()
    if(s.count(".") != 1 ):
        print(False)
        continue
    try:
        float(s)
        print(True)
    except ValueError:
        print(False)
'''
