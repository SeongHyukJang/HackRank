# Enter your code here. Read input from STDIN. Print output to STDOUT
size = input().split(" ")
for i in range(2):
    size[i] = int(size[i])
for i in range(int(size[0])):
    if i < (size[0]-1)/2 :
        print((".|."*(2*i+1)).center(size[1],"-"))
    elif i == (size[0]+1)/2:
        print("WELCOME".center(size[1],"-"))

for i in range(int(size[0]),-1,-1):
    if i < (size[0]-1)/2 :
        print((".|."*(2*i+1)).center(size[1],"-"))

