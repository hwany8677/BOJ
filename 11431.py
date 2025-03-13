#No diagonal lines, meaning every wall is perpendicular
input=open(0).readline
for k in range(int(input())):
    n,s,p=map(int,input().split())
    xi,yi=map(int,input().split())
    l=0
    for _ in range(n-1):
        xi_1,yi_1=map(int,input().split())
        if xi==xi_1: l+=
