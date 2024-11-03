from collections import deque
input=open(0).readline
def BFS(nodes,first_visit,visited):
    buf=deque([first_visit])
    count=len(buf)
    to_visit=0
    remaining=len(buf)
    for node in buf: visited[node]=True
    while(count>0):
        visiting=buf.popleft()
        remaining-=1
        count-=1
        for node in nodes[visiting]:
            if visited[node]: continue
            else:
                visited[node]=True
                buf.append(node)
                count+=1
                to_visit+=1
        if remaining==0:
            remaining=to_visit
            to_visit=0
    return visited
n,m=map(int,input().split())
nodes=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)
visited=[False]*(n+1)
visited=BFS(nodes,1,visited)
if sum(visited)==n: print(0)
else:
    for i in range(1,n+1):
        if not(visited[i]): print(i)