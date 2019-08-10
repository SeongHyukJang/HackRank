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
