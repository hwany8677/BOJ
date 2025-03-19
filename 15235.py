#나이브 브포?
#이게 되네
n=int(input())
buf=list(map(int,input().split()))
sigma=sum(buf)
time=[0 for _ in range(len(buf))]
i,t=0,1
while(sigma>0):
    if buf[i]>0: 
        buf[i]-=1
        sigma-=1
        if buf[i]==0: time[i]+=t
    else: 
        i+=1
        if i==n: i=0
        continue
    i+=1
    if i==n: i=0
    t+=1
print(*time)
