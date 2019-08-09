if __name__ == '__main__':
    s = input()
res = False
for i in s:
    if i.isalnum() == True:
        res = res or True
    else:
        res = res or False
print(res)

res = False
for i in s:
    if i.isalpha() == True:
        res = res or True
    else:
        res = res or False
print(res)

res = False
for i in s:
    if i.isdigit() == True:
        res = res or True
    else:
        res = res or False
print(res)

res = False
for i in s:
    if i.islower() == True:
        res = res or True
    else:
        res = res or False
print(res)

res = False
for i in s:
    if i.isupper() == True:
        res = res or True
    else:
        res = res or False
print(res)
