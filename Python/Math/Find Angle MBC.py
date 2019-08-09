# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = int(input())
BC = int(input())
AC = math.sqrt(pow(AB,2)+pow(BC,2))
BM = AC/2
MC = AC/2
S = (1/2)*AB*BC
theta = math.asin(S/(BM*BC))
print(format(math.degrees(theta),".0f")+"°")
