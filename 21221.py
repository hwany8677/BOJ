from copy import deepcopy
input=open(0).readline
n,m=map(int,input().split())
buf=[]
for _ in range(n): buf.append(list(input().rstrip()))
output_buf=deepcopy(buf)
for i in range(n):
    for j in range(m):
        if buf[i][j]=='#': output_buf[i+1][j],output_buf[i][j+1],output_buf[i+1][j+1]='#','#','#'
for i in range(n): print(*output_buf[i],sep='')
