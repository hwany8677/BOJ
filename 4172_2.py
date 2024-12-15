#Initial code, had a fair amount of overhead
input=open(0).readline
from math import floor,sqrt,log,sin #log(2) is ln(2) by default
x=[1]
for i in range(1,1000001):
    first=floor(i-sqrt(i))
    second=floor(log(i))
    third=floor(((sin(i))**2)*i)
    x.append(x[first]+x[second]+x[third])
n=int(input())
while(n!=-1):
    print(x[n]%1000000)
    n=int(input())
