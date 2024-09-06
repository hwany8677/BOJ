n,k=map(int,input().split())
buf=[i for i in range(1,n+1)]
res=[]
count=k
while(sum(buf)>-n):
    for i in range(n):
        if buf[i]==-1: continue
        if buf[i]>0: count-=1
        if count==0:
            res.append(buf[i])
            buf[i]=-1
            count=k
res=str(res).strip('[').strip(']')
print('<',res,'>',sep='')