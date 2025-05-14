#TLE on 89%, doesn't work
input=open(0).readline
n=int(input())
a=list(map(int,input().split()))
m=int(input())
for _ in range(m):
    query=list(map(int,input().split()))
    if len(query)==4: cmd,i,j,k=query[0],query[1]-1,query[2]-1,query[3]
    else: cmd,i,k=query[0],query[1]-1,query[2]
    if cmd==2: a[i]=k
    else:
        count=0
        for idx in range(i,j+1):
            if a[idx]>k: count+=1
        print(count)