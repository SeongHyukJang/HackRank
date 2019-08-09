# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
num = int(input())

for i in range(num):
    case = input()
    try:
        res = re.compile(case)
        print("True")
    except:
        print("False")
