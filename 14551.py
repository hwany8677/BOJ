n,m=map(int,input().split())
combi=1
for i in range(n):
    buf=int(input())
    combi*=buf if buf!=0 else 1
print(combi%m)