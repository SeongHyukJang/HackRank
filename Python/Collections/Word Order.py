# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
n = int(input())
counter = 0
WordsList = []
while counter != n:
    WordsList.append(input())
    counter +=1
x = collections.Counter(WordsList)
print(len(x))
for i in x.values():
    print(i,end = ' ')
