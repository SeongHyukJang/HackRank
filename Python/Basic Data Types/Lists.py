if __name__ == '__main__':
    N = int(input())
    res = []
    for i in range(N):
        x = input().split(" ")
        if x[0] == "print":
            print(res)
        elif x[0] == "sort":
            res = sorted(res)
        elif x[0] == "pop":
            res.pop()
        elif x[0] == "reverse":
            res = res[::-1]
        elif x[0] == "insert":
            place = int(x[1])
            res1 = res[:place]
            res2 = res[place:]
            res = res1 + [int(x[2])] + res2
        elif x[0] == "remove":
            res.remove(int(x[1]))
        elif x[0] == "append":
            res.append(int(x[1]))
