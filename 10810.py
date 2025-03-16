#Naive
input=open(0).readline
n,m=map(int,input().split())
ball=[0 for _ in range(n)]
for _ in range(m):
    i,j,k=map(int,input().split())
    for idx in range(i,j+1): ball[idx-1]=k
print(*ball)