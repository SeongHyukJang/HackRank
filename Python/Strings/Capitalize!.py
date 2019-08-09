# Complete the solve function below.
def solve(s):
    res = ""
    s = s.split(" ")
    for i in s:
        res += " " + i.capitalize()
    return res.strip(" ")
