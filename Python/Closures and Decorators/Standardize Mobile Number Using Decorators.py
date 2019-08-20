def wrapper(f):
    def fun(l):
        s = "+91 "
        for i in range(len(l)):
            if len(l[i]) == 10:
                l[i] = s + l[i][:5] + " " + l[i][5:]
            elif l[i][0] == '+':
                l[i] = s + l[i][3:8] + " "  + l[i][8:]
            elif l[i][0] == '0':
                l[i] = s + l[i][1:6] + " " + l[i][6:]
            elif l[i][:2] == '91':
                l[i] = s + l[i][2:7] + " " + l[i][7:]
        f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)