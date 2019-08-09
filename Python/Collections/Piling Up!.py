# Enter your code here. Read input from STDIN. Print output to STDOUT
TestCases = int(input())
counter = 0
while counter != 2*TestCases:
    N = int(input())
    Cube = list(map(int,input().split()))
    LeftSide = Cube[:Cube.index(min(Cube))]
    RightSide = Cube[Cube.index(min(Cube)):]
    if LeftSide == sorted(LeftSide,reverse = True) and RightSide == sorted(RightSide):
        print("Yes")
    else:
        print("No")
    counter += 2
