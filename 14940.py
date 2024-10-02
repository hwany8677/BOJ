from collections import deque
from sys import stdin
input=stdin.readline

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
def predeces_btrack(josang,buf,visited): #visited를 사용하여 한번 간 경로는 못가도록 막아놓기
    length=len(visited)
    n,m=len(buf),len(buf[0])
    res=[0 for _ in range(length)] #저장할때는 1차원, 출력할때는 2차원
    while(1):
        for idx_1 in range(n-1,-1,-1):
            to_break=False
            for idx_2 in range(m-1,-1,-1):
                if buf[idx_1][idx_2]==2: return res
                if buf[idx_1][idx_2]!=0 and visited[(m*idx_1)+idx_2]==True:
                    i=(m*idx_1)+idx_2
                    to_break=True
                    break
            if to_break: break
        count=0
        while(i!=-1):
            # print(f"{josang[i]} -> ",end='')
            count+=1
            visited[i]=False
            res[i]=count
            i=josang[i]
    return
n,m=map(int,input().split())
buf=[]
for _ in range(n): buf.append(list(map(int,input().split())))
nodes=[[] for _ in range(n*m)]
visited=[False]*(n*m)
pred=[-1 for _ in range(n*m)]
for i in range(n):
    for j in range(m):
        node_no=(m*i)+j
        current=buf[i][j]
        if j<m-1:
            if node_no==0 or (buf[i][j+1]==1 and current==1):
                nodes[node_no].append(node_no+1)
                nodes[node_no+1].append(node_no)
        if i<n-1:
            if node_no==0 or (buf[i+1][j]==1 and current==1):
                nodes[node_no].append(node_no+m)
                nodes[node_no+m].append(node_no)
        if current==0: visited[node_no]=True
visited,pred=BFS(nodes,0,visited,pred)
res=predeces_btrack(pred,buf,visited)
#print
for i in range(n*m):
    print(f"{res[i]} ",end='')
    if (i+1)%m==0: print()