#교훈: 괄호는 사기다.
from math import sqrt
for _ in range(int(input())):
    a,b,c=map(float,input().split())
    x1=(-b+sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-sqrt(b**2-4*a*c))/(2*a)
    print("{:.3f},".format(x1), "{:.3f}".format(x2))