# Enter your code here. Read input from STDIN. Print output to STDOUT
TheNumberOfShoes = input()
ShoeSizes = list(input().split(" "))
Customers = int(input())
res = 0
for i in range(Customers):
    ShoeSize, Price = input().split(" ")
    if ShoeSize in ShoeSizes:
        res += int(Price)
        ShoeSizes.remove(ShoeSize)
print(res)
