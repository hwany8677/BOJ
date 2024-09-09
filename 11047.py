#기본적인 그리디 문제
from sys import stdin
input=stdin.readline

n,k=map(int,input().split())
value=[]
count=0
for _ in range(n): value.append(int(input()))
for i in range(n-1,-1,-1):
    if value[i]>k: continue
    elif value[i]<k:
        k-=value[i]
        count+=1
print(count)
