#조상을 찾아 빠르게 가는 문제
from collections import deque
from sys import stdin
input=stdin.readline

def BFS(nodes,first_visit,visited):
    buf=deque(first_visit)
    count=len(buf)
    tries=0
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
            tries+=1
            remaining=to_visit
            to_visit=0
    return tries,visited
m,n=map(int,input().split())
buf=[]
total_conquer=n*m #-1을 제외한 정복필요개수
for _ in range(n): buf.append(input().split())
nodes=[[] for _ in range(n*m)]
visited=[False]*(n*m)
first_visit=[]
has_zero=False
for i in range(n):
    for j in range(m):
        node_no=(m*i)+j
        current=buf[i][j]
        if current=='1': first_visit.append(node_no)
        if current=='-1': visited[node_no]=True
        if current=='0': has_zero=True
        if j<m-1:
            if (buf[i][j+1]=='0' or buf[i][j+1]=='1') and (current=='0' or current=='1'):
                nodes[node_no].append(node_no+1)
                nodes[node_no+1].append(node_no)
        if i<n-1:
            if (buf[i+1][j]=='0' or buf[i+1][j]=='1') and (current=='0' or current=='1'):
                nodes[node_no].append(node_no+m)
                nodes[node_no+m].append(node_no)
if not(has_zero): 
    print(0)
    exit(0)
res,visited=BFS(nodes,first_visit,visited)
if sum(visited)==total_conquer: print(res-1)
else: print(-1)