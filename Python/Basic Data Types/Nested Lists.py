if __name__ == '__main__':
    res_list = []
    score_set = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        res_list.append([name,score])
        score_set.add(score)
score_list = sorted(list(score_set))
target = score_list[1]
for i in sorted(res_list):
    if target in i:
        print(i[0])
