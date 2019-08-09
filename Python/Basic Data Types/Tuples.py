if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
res = []
for i in integer_list:
    res.append(i)
print(hash(tuple(res)))
