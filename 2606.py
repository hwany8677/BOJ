from collections import deque
from sys import stdin
input=stdin.readline

def hello_your_computer_has_virus(nodes,visited):
    buf=deque([1])
    count=1
    while(count>0):
        visiting=buf.popleft()
        visited[visiting]=True
        count-=1
        for node in nodes[visiting]:
            if visited[node]: continue
            else:
                visited[node]=True
                buf.append(node)
                count+=1
    infected=sum(visited)-1
    return infected
n=int(input())
m=int(input())
nodes=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)
for i in range(1,n+1): nodes[i].sort()
visited=[False]*(n+1)
print(hello_your_computer_has_virus(nodes,visited))