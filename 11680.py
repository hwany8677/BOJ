#dN, dM
n,m=map(int,input().split())
dn=[i for i in range(1,n+1)]
dm=[i for i in range(1,m+1)]
s=[]
for i in dn:
    for j in dm: s.append(i+j)
res=dict()
for i in s:
    if i in res: res[i]+=1
    else: res[i]=1
mx=res[max(res,key=res.get)]
for i in list(res.items()):
    if i[1]==mx: print(i[0])