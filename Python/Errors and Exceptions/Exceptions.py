# Enter your code here. Read input from STDIN. Print output to STDOUT
TestCases = int(input())
counter = 0
while counter != TestCases:
    a,b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as E:
        print("Error Code:",E)
    except ValueError as V:
        print("Error Code:",V)
    counter +=1
