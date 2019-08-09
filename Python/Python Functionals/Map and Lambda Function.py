cube = lambda x:pow(x,3) 

def fibonacci(n):
    if n == 0:
        res = []
    elif n == 1:
        res = [0]
    else:
        res = [0,1]
        counter = 2
        while counter != n:
            res.append(res[-1]+res[-2])
            counter += 1
    return res
