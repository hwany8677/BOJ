from collections import deque
from sys import stdin
input=stdin.readline

#0 1 6 7 12 13 18 14 19 15 20 9 16 21 3 10 17 4 23
def BFS(nodes,first_visit,visited,josang):
    buf=deque([first_visit])
    count=1
    visited[0]=True
    while(count>0):
        visiting=buf.popleft()
        josang_daesang=visiting
        # print(visiting,end=' ')
        count-=1
        for node in nodes[visiting]:
            if visited[node]: continue
            else: 
                visited[node]=True
                josang[node]=josang_daesang
                buf.append(node)
                count+=1
    return visited,josang
def predeces_btrack(josang):
    i=len(josang)-1
    count=0
    while(i!=-1):
        count+=1
        i=josang[i]
    return count
n,m=map(int,input().split())
buf=[]
for _ in range(n): buf.append(input().rstrip())
nodes=[[] for _ in range(n*m)]
visited=[False]*(n*m)
pred=[-1 for _ in range(n*m)] #n번째의 조상은 누구!? (-1 = Invalid)
for i in range(n):
    for j in range(m):
        node_no=(m*i)+j
        current=buf[i][j]
        if j<m-1:
            if buf[i][j+1]=='1' and current=='1':
                nodes[node_no].append(node_no+1)
                nodes[node_no+1].append(node_no)
        if i<n-1:
            if buf[i+1][j]=='1' and current=='1':
                nodes[node_no].append(node_no+m)
                nodes[node_no+m].append(node_no)
        if current=='0': visited[node_no]=True
visited,pred=BFS(nodes,0,visited,pred)
print(predeces_btrack(pred))