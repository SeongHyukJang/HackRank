# Enter your code here. Read input from STDIN. Print output to STDOUT
num = complex(input())
from cmath import phase
from math import sqrt
print(sqrt(pow(num.real,2)+pow(num.imag,2)))
print(phase(num))
