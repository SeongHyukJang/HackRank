def merge_the_tools(string, k):
    # your code goes here
    i = 0
    while i != len(string):
        res = list(string[i:i+k])
        res.reverse()
        ResSet = set(res)
        for j in ResSet:
            while res.count(j) != 1:
                res.remove(j)
        res.reverse()
        print(''.join(res))
        i += k
