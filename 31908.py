#이거 걍 탐색해야됨??
from sys import stdin
input=stdin.readline

n=int(input())
rings=[]
members=[]
for _ in range(n):
    a,b=input().split()
    members.append(a)
    rings.append(b)
couples=0
i=0
buf=[]
visited=[False]*n
while(i<n):
    if rings[i]=='-': 
        i+=1
        continue

    mem_cur,ring_cur=members[i],rings[i]
    mem_match,ring_match='',''
    count=1
    visited[i]=True

    for j in range(n):
        if i==j: continue
        if visited[j]: continue

        if rings[j]==ring_cur:
            count+=1
            mem_match=members[j]
            visited[j]=True
    
    if count==2:
        buf.append([mem_cur,mem_match])
        couples+=1
    i+=1
print(couples)
for i in range(len(buf)): print(*buf[i])