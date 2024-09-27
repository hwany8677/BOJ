#676ms, a bit distant from average
from collections import deque
from sys import stdin
input=stdin.readline

def BFS(nodes,first_visit,visited):
    buf=deque([first_visit])
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
    return visited
n,m=map(int,input().split())
nodes=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)
for i in range(1,n+1): nodes[i].sort()
visited=[False]*(n+1)
visited[0]=True
#visited[i]=False 되는 노드를 찾기
startpoint=1
visited=BFS(nodes,startpoint,visited)
count=1
while(1):
    if sum(visited)==(n+1): break
    else:
        for i in range(1,n+1):
            if visited[i]==False: startpoint=i; break
    visited=BFS(nodes,startpoint,visited)
    count+=1
print(count)