from collections import deque
from sys import stdin
input=stdin.readline

#0 1 6 7 12 13 18 14 19 15 20 9 16 21 3 10 17 4 23
def BFS(nodes,first_visit,visited):
    buf=deque([first_visit])
    count=1
    steps_taken=0
    steptake_delay=1
    visited[0]=True
    while(count>0):
        visiting=buf.popleft()
        steptake_delay-=1
        print(visiting,end=' ')
        count-=1
        if steptake_delay==0: steps_taken+=1
        for node in nodes[visiting]:
            if visited[node]: continue
            else: 
                visited[node]=True
                buf.append(node)
                count+=1
                steptake_delay+=1
    print(f"\nsteps_taken={steps_taken}")
    return visited
n,m=map(int,input().split())
buf=[]
for _ in range(n): buf.append(input().rstrip())
nodes=[[] for _ in range(n*m)]
visited=[False]*(n*m)
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
visited=BFS(nodes,0,visited)
