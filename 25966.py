input=open(0).readline
n,m,q=map(int,input().split())
buf=[]
for _ in range(n): buf.append(list(map(int,input().split())))
for _ in range(q):
    query=list(map(int,input().split()))
    cmd=query[0]
    i,j=query[1],query[2]
    if len(query)==4: k=query[3]
    if cmd==0: buf[i][j]=k
    if cmd==1: buf[i],buf[j]=buf[j],buf[i]
for row in buf: print(*row)
