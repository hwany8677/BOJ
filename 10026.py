#Naive? method 
#But it works!
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
def prep(buf):
    #노드 등록 -> (n*i+j) 번째
    #탐색 시 오른쪽과 아래만 볼것
    #0 1 2 3 4
    #5 6 7 8 9
    #10 11 12 13 14
    #...
    nodes=[[] for _ in range(n*n)]
    letter=buf[0][0]
    for i in range(n):
        for j in range(n):
            node_no=(n*i)+j
            if buf[i][j]!=letter: letter=buf[i][j]
            #오른쪽과 아래로 보기
            #IndexError 방지
            if j<n-1:
                if buf[i][j+1]==letter: 
                    nodes[node_no].append(node_no+1)
                    nodes[node_no+1].append(node_no)
            if i<n-1:
                if buf[i+1][j]==letter: 
                    nodes[node_no].append(node_no+n)
                    nodes[node_no+n].append(node_no)
    startpoint=0
    visited=[False]*(n*n)
    visited=BFS(nodes,startpoint,visited)
    node_posX=(i//5)
    node_posY=(i%5)
    letter=buf[node_posX][node_posY]
    count=1
    while(1):
        if sum(visited)==(n*n): break
        else:
            for i in range(n*n):
                if visited[i]==False: 
                    startpoint=i
                    break
        visited=BFS(nodes,startpoint,visited)
        count+=1
    print(count,end='')
    return nodes
n=int(input())
buf=[]
for _ in range(n): buf.append(list(input().rstrip()))
nodes=prep(buf)
for i in range(n):
    for j in range(n):
        if buf[i][j]=='G': buf[i][j]='R'
print(" ",end='')
prep(buf)
print()