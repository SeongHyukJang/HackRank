NumberOfElementsInA = int(input())
A = set(input().split())
N = int(input())
counter = 0
while counter != 2*N:
    command = input().split()
    elements = set(input().split())
    if command[0] == "intersection_update":
        A &= elements
    if command[0] == "update":
        A |= elements
    if command[0] == "symmetric_difference_update":
        A ^= elements
    if command[0] == "difference_update":
        A -= elements
    counter += 2

print(sum(map(int,A)))
