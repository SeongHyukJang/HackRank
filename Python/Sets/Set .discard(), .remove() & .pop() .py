n = int(input())
s = set(map(int, input().split()))
commands = int(input())
counter = 0
while counter != commands:
    command = input().split()
    if command[0] == "pop":
        s.pop()
    if command[0] == "remove":
        s.remove(int(command[1]))
    if command[0] == "discard":
        s.discard(int(command[1]))
    counter += 1
res = 0
for i in s:
    res += i

print(res)
