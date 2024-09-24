from sys import stdin
input=stdin.readline

for _ in range(int(input())):
    buf=list(map(int,input().split()))
    res=[0 for _ in range(20)]
    for i in range(19,0,-1):
        temp=buf[i]
        res[i]+=temp%2
        buf[i-1]+=temp//2
res[0]=buf[0]
print(*res)
