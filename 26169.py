# 0  1  2  3  4
#...
#20 21 22 23 24
#      ||
#      ||
#      vv
#00 01 02 03 04
#...
#40 41 42 43 44 (node//5,node%5)
from collections import deque
from copy import copy
input=open(0).readline
def BFS(nodes,first_visit,visited,gridmap):
    buf=deque([first_visit])
    steps=3
    count=1
    while(count>0):
        cur_visit=buf.popleft()
        visited[cur_visit]=True
        count-=1
        for node in nodes[cur_visit]:
            r,c=node//5,node%5
            if visited[node]: continue
            else:
                visited[node]=True
                buf.append(node)
                count+=1
    return visited
nodes=deque([[] for _ in range(25)])
visited=[False]*(25)
buf=[]
for _ in range(5): buf.append(list(map(int,input().split())))
for i in range(5):
    for j in range(5):
        node_no=5*i+j
        current=buf[i][j]
        if current==-1: visited[node_no]=True; continue
        if j<4:
            if (buf[i][j+1]==0 or buf[i][j+1]==1) and (current==0 or current==1):
                nodes[node_no].append(node_no+1)
                nodes[node_no+1].append(node_no)
        if i<4:
            if (buf[i+1][j]==0 or buf[i+1][j]==1) and (current==0 or current==1):
                nodes[node_no].append(node_no+5)
                nodes[node_no+5].append(node_no)
r,c=map(int,input().split())
first_visit=5*r+c
BFS(nodes,first_visit,visited,buf)