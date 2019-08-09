# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
res = deque()
num = int(input())
counter = 0
while counter != num:
    command = input().split()
    if command[0] == 'append':
        res.append(command[1])
    elif command[0] == 'appendleft':
        res.appendleft(command[1])
    elif command[0] == 'pop':
        res.pop()
    elif command[0] == 'popleft':
        res.popleft()
    counter +=1
print(' '.join(res))
