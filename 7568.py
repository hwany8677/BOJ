from copy import copy
n=int(input())
info=[]
for _ in range(n): 
    x,y=map(int,input().split())
    info.append((x,y))
info_copy=copy(info)
info_copy.sort(key=lambda x:x[1])
info_copy.reverse()
res=[1]
w_mn,h_mn=info_copy[0][0],info_copy[0][1]
i=1
pos=1
while(i<len(info_copy)):
    cond=0
    weight=info_copy[i][0]
    height=info_copy[i][1]
    if weight<w_mn: 
        w_mn=weight
        cond+=1
    if height<h_mn: 
        h_mn=height
        cond+=1
    if cond==2: pos=i+1
    res.append(pos)
    i+=1
for element in info:
    buf=res[info_copy.index(element)]
    print(buf,end=' ')
print()