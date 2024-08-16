from sys import stdin
input=stdin.readline
n,k=map(int,input().split())
buf=[]
c=0
for _ in range(n): buf.append(int(input()))
for i in range(1,n):
    delta=buf[i-1]-buf[i]
    if delta>=k: c+=1
print(c)