input=open(0).readline
for i in range(1,1+int(input())):
    n,m=map(int,input().split())
    buf=[[0 for __ in range(n+1)] for _ in range(n+1)]
    for _ in range(m):
        fromm,to=map(int,input().split())
        if fromm>to: fromm,to=to,fromm
        buf[fromm][to]=1
    s=int(input())
    print(f"Data Set {i}:")
    for i in range(n+1):
        element=buf[s][i]
        if element==1: print(i,end=' ')
    print('\n')
