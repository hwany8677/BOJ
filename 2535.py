input=open(0).readline
n=int(input())
gukga,haksaeng,score=[],[],[]
gukga_count=[0 for _ in range(n+1)] #1번부터 n번까지
for i in range(1,n+1):
    a,b,c=map(int,input().split())
    gukga.append(a); haksaeng.append(b)
    score.append(c);
buf=list(zip(gukga,haksaeng,score))
buf.sort(key=lambda tup: tup[2],reverse=True)
res=[]
mn=1001; awards=0
for data in buf:
    if awards==3: break
    where=data[0]
    who=data[1]
    scored=data[2]
    if gukga_count[where]<2:
        gukga_count[where]+=1
        if scored<mn:
            mn=scored
            awards+=1
            res.append([where,who])
for result in res: print(*result)
