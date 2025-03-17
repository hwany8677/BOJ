#No diagonal lines, meaning every wall is perpendicular
#Thus, the wall is made so that it does not make an area
from math import ceil
input=open(0).readline
for k in range(int(input())):
    #n: number of sides
    #s: number of hours required for a single person to take down 1m of wall
    #p: number of people
    n,s,p=map(int,input().split())
    xi,yi=map(int,input().split())
    l=0
    time=0
    for _ in range(n):
        xi_1,yi_1=map(int,input().split())
        if xi==xi_1: l+=abs(yi_1-yi)
        elif yi==yi_1: l+=abs(xi_1-xi)
        xi,yi=xi_1,yi_1
    temp=s/p
    time=l*temp
    print(f"Data Set {k+1}: ")
    print(ceil(time))
    print()
