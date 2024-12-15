#floor 쓰지말고 int()쓰는 습관을 들이기
input=open(0).readline
from math import sqrt,log,sin #log(2) is ln(2) by default
x=[1]*(1000001)
for i in range(1,1000001):
    first=int(i-sqrt(i))
    second=int(log(i))
    third=int(((sin(i))**2)*i)
    x[i]=(x[first]+x[second]+x[third])%1000000
n=int(input())
while(n!=-1):
    print(x[n])
    n=int(input())
