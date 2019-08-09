# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
NumberOfSets = int(input())
res = True
counter = 0
while counter != NumberOfSets:
    OtherSet = set(input().split())
    if OtherSet == A:
        res = res and False
    elif OtherSet != OtherSet&A:
        res = res and False
    else:
        res = res and True
    counter += 1
print(res)
