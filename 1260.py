#Recursion method (DFS)
from collections import deque
from sys import stdin
input=stdin.readline

def BFS(nodes,first_visit,visited):
    buf=deque([first_visit])
    count=1
    output_buf=[]
    while(count>0):
        visiting=buf.popleft()
        visited[visiting]=True
        count-=1
        output_buf.append(visiting)
        for node in nodes[visiting]:
            if visited[node]: continue
            else:
                visited[node]=True
                buf.append(node)
                count+=1
    return output_buf
def DFS(nodes,visiting,visited):
    visited[visiting]=True
    print(visiting,end=' ')
    for node in nodes[visiting]:
        if not(visited[node]): DFS(nodes,node,visited)
        else: continue
    return 0
n,m,v=map(int,input().split())
nodes=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)
for i in range(1,n+1): nodes[i].sort()
DFS(nodes,v,visited)
visited=[False]*(n+1)
print()
print(*BFS(nodes,v,visited))