n=int(input())
count=[0 for _ in range(n)]
buf=list(map(int,input().split()))
for element in buf: 
    if element==0: continue
    count[element-1]+=1
mx=max(count)
mxs=0
for crew in count:
    if crew==mx: mxs+=1
if mxs==1: print(count.index(mx)+1)
else: print("skipped")