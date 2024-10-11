################################ 하이퍼 ################################
# 하                             하이퍼                               하
#
# 이                             하이퍼                               이
#
# 퍼                             하이퍼                               퍼
################################ 하이퍼 ################################
from time import process_time as pt,perf_counter as pf
from collections import deque
input=open(0).readline

def BFS(nodes,first_visit,visited):
    t0=pf()

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
            ## TEST CODE ##
            t=pf()
            if (t-t0>4.8): exit(1)
            ## TEST CODE ##
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
w,v,u,t,s,r,q,p,o,n,m=map(int,input().split())
buf=deque()
total_conquer=m*n*o*p*q*r*s*t*u*v*w
for a in range(m): 
    buf.append([])
    for b in range(n):
        buf[a].append([])
        for c in range(o):
            buf[a][b].append([])
            for d in range(p):
                buf[a][b][c].append([])
                for e in range(q):
                    buf[a][b][c][d].append([])
                    for f in range(r):
                        buf[a][b][c][d][e].append([])
                        for g in range(s):
                            buf[a][b][c][d][e][f].append([])
                            for h in range(t):
                                buf[a][b][c][d][e][f][g].append([])
                                for i in range(u):
                                    buf[a][b][c][d][e][f][g][h].append([])
                                    for j in range(v): 
                                        buf[a][b][c][d][e][f][g][h][i].append(input().split())
nodes=deque()
nodes=deque([] for _ in range(m*n*o*p*q*r*s*t*u*v*w))
visited=deque([False]*(m*n*o*p*q*r*s*t*u*v*w))
first_visit=deque()
has_zero=False
for a in range(m): 
    for b in range(n):
        for c in range(o):
            for d in range(p):
                for e in range(q):
                    for f in range(r):
                        for g in range(s):
                            for h in range(t):
                                for i in range(u):
                                    for j in range(v):
                                        for k in range(w):
                                            node_no=(
                                                a*n*o*p*q*r*s*t*u*v*w+
                                                b*o*p*q*r*s*t*u*v*w+
                                                c*p*q*r*s*t*u*v*w+
                                                d*q*r*s*t*u*v*w+
                                                e*r*s*t*u*v*w+
                                                f*s*t*u*v*w+
                                                g*t*u*v*w+
                                                h*u*v*w+
                                                i*v*w+
                                                j*w+
                                                k
                                            )
                                            current=buf[a][b][c][d][e][f][g][h][i][j][k]
                                            if current=='1': first_visit.append(node_no)
                                            if current=='-1': visited[node_no]=True
                                            if current=='0': has_zero=True
                                            if a<m-1:
                                                if (buf[a+1][b][c][d][e][f][g][h][i][j][k]=='0' or buf[a+1][b][c][d][e][f][g][h][i][j][k]=='1') and (current=='0' or current=='1'):
                                                    nodes[node_no].append(node_no+n*o*p*q*r*s*t*u*v*w)
                                                    nodes[node_no+n*o*p*q*r*s*t*u*v*w].append(node_no)
                                            if b<n-1:
                                                if (buf[a][b+1][c][d][e][f][g][h][i][j][k]=='0' or buf[a][b+1][c][d][e][f][g][h][i][j][k]=='1') and (current=='0' or current=='1'):
                                                    nodes[node_no].append(node_no+o*p*q*r*s*t*u*v*w)
                                                    nodes[node_no+o*p*q*r*s*t*u*v*w].append(node_no)
                                            if c<o-1:
                                                if (buf[a][b][c+1][d][e][f][g][h][i][j][k]=='0' or buf[a][b][c+1][d][e][f][g][h][i][j][k]=='1') and (current=='0' or current=='1'):
                                                    nodes[node_no].append(node_no+p*q*r*s*t*u*v*w)
                                                    nodes[node_no+p*q*r*s*t*u*v*w].append(node_no)
                                            if d<p-1:
                                                if (buf[a][b][c][d+1][e][f][g][h][i][j][k]=='0' or buf[a][b][c][d+1][e][f][g][h][i][j][k]=='1') and (current=='0' or current=='1'):
                                                    nodes[node_no].append(node_no+q*r*s*t*u*v*w)
                                                    nodes[node_no+q*r*s*t*u*v*w].append(node_no)
                                            if e<q-1:
                                                if (buf[a][b][c][d][e+1][f][g][h][i][j][k]=='0' or buf[a][b][c][d][e+1][f][g][h][i][j][k]=='1') and (current=='0' or current=='1'):
                                                    nodes[node_no].append(node_no+r*s*t*u*v*w)
                                                    nodes[node_no+r*s*t*u*v*w].append(node_no)
                                            if f<r-1:
                                                if (buf[a][b][c][d][e][f+1][g][h][i][j][k]=='0' or buf[a][b][c][d][e][f+1][g][h][i][j][k]=='1') and (current=='0' or current=='1'):
                                                    nodes[node_no].append(node_no+s*t*u*v*w)
                                                    nodes[node_no+s*t*u*v*w].append(node_no)
                                            if g<s-1:
                                                if (buf[a][b][c][d][e][f][g+1][h][i][j][k]=='0' or buf[a][b][c][d][e][f][g+1][h][i][j][k]=='1') and (current=='0' or current=='1'):
                                                    nodes[node_no].append(node_no+t*u*v*w)
                                                    nodes[node_no+t*u*v*w].append(node_no)
                                            if h<t-1:
                                                if (buf[a][b][c][d][e][f][g][h+1][i][j][k]=='0' or buf[a][b][c][d][e][f][g][h+1][i][j][k]=='1') and (current=='0' or current=='1'):
                                                    nodes[node_no].append(node_no+u*v*w)
                                                    nodes[node_no+u*v*w].append(node_no)
                                            if i<u-1:
                                                if (buf[a][b][c][d][e][f][g][h][i+1][j][k]=='0' or buf[a][b][c][d][e][f][g][h][i+1][j][k]=='1') and (current=='0' or current=='1'):
                                                    nodes[node_no].append(node_no+v*w)
                                                    nodes[node_no+v*w].append(node_no)
                                            if j<v-1:
                                                if (buf[a][b][c][d][e][f][g][h][i][j+1][k]=='0' or buf[a][b][c][d][e][f][g][h][i][j+1][k]=='1') and (current=='0' or current=='1'):
                                                    nodes[node_no].append(node_no+w)
                                                    nodes[node_no+w].append(node_no)
                                            if k<w-1:
                                                if (buf[a][b][c][d][e][f][g][h][i][j][k+1]=='0' or buf[a][b][c][d][e][f][g][h][i][j][k+1]=='1') and (current=='0' or current=='1'):
                                                    nodes[node_no].append(node_no+1)
                                                    nodes[node_no+1].append(node_no)
if not(has_zero): 
    print(0)
    exit(0)
res,visited=BFS(nodes,first_visit,visited)
if sum(visited)==total_conquer: print(res-1)
else: print(-1)