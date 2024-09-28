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
    visited=[False]*(n*m)
    for _ in range(k): 
        hor,ver=map(int,input().split()) #가로, 세로
        buf[ver][hor]=1
    for i in range(n):
        for j in range(m):
            current=buf[i][j]
            node_no=(m*i)+j
            has_adjacent=False
            if j<m-1 and current==1:
                if buf[i][j+1]==1:
                    nodes[node_no].append(node_no+1)
                    nodes[node_no+1].append(node_no)
                    has_adjacent=True
            if i<n-1 and current==1:
                if buf[i+1][j]==1:
                    nodes[node_no].append(node_no+m)
                    nodes[node_no+m].append(node_no)
                    has_adjacent=True
            if not(has_adjacent): 
                if current==1: nodes[node_no].append(node_no)
                else: visited[node_no]=True #Visited로 둠으로써 탐색을 방지
    startpoint=0
    count=0
    last_point=0
    while(1):
        for i in range(last_point-1,n*m):
            if visited[i]==False:
                startpoint=i
                last_point=i
                break
        visited=BFS(nodes,startpoint,visited)
        count+=1
        if sum(visited)==(n*m): break
    print(count)