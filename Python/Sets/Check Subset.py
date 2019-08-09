# Enter your code here. Read input from STDIN. Print output to STDOUT
TestCases = int(input())
counter = 0
while counter != 4*TestCases:
    A_elements = int(input())
    A = set(input().split())
    B_elements = int(input())
    B = set(input().split())
    if A == A&B:
        print(True)
    else:
        print(False)
    counter += 4
