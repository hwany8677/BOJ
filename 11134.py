input=open(0).readline
t=int(input())
for _ in range(t):
    n,c=map(int,input().split())
    count=n//c
    count+=1 if n%c>0 else 0
    print(count)