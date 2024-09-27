#Non-recursion method (DFS)
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
def DFS(nodes,first_visit,visited):
    n,count=len(visited),0
    visit_stack=[first_visit]
    while(1):
        has_somewhere=False
        visiting=visit_stack[count]
        for node in nodes[visiting]:
            if visited[node]: continue
            else:
                has_somewhere=True
                visit_stack.append(node)
                count+=1
                break
        if not(has_somewhere):
            if visiting==first_visit: break
            visit_stack.pop(count)
            count-=1
        if not(visited[visiting]): print(visiting,end=' ')
        visited[visiting]=True
    return 0
n,m,v=map(int,input().split())
nodes=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)
for i in range(1,n+1): nodes[i].sort()
#Temporary fix, will need to redo the whole code for other problems
if len(nodes[v])==0: print(v)
else: 
    DFS(nodes,v,visited)
    print()
visited=[False]*(n+1)
print(*BFS(nodes,v,visited))