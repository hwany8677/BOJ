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
for _ in range(int(input())):
    # n m - - - - - - - ->
    # |
    # | 진자 햇깔려 죽겠네
    # |
    # v
    m,n,k=map(int,input().split()) #가로(m), 세로(n)
    buf=[[0 for _ in range(m)] for _ in range(n)]
    nodes=[[] for _ in range(m*n)]
    for _ in range(k): 
        hor,ver=map(int,input().split()) #가로, 세로
        buf[ver][hor]=1
    for i in range(n):
        for j in range(m):
            node_no=(m*i)+j
            if j<n-1:
                if buf[i][j+1]==1:
                    nodes[node_no].append(node_no+1)
                    nodes[node_no+1].append(node_no)
            if i<n-1:
                if buf[i+1][j]==1:
                    nodes[node_no].append(node_no+n)
                    nodes[node_no+n].append(node_no)
    startpoint=0
    visited=[False]*(n*m)
    visited=BFS(nodes,startpoint,visited)
    count=1
    while(1):
        if sum(visited)==(n*m): break
        else:
            for i in range(n*m):
                if visited[i]==False:
                    startpoint=i
                    break
        visited=BFS(nodes,startpoint,visited)
        count+=1
    print(count)