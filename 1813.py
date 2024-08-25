#Filthy code
#난애드혹을못하는게맞아요
#난이걸시발이틀이나고민한게존나게후회된ㄱ다
n=int(input())
buf=list(map(int,input().split()))
bindo_su=[0 for _ in range(51)]
if len(buf)==1:
    #1
    #1
    if buf[0]==1: print(1)
    #1
    #(대충1이아닌0이아닌음수)
    else: print(-1)
    exit(0)
buf.sort()
for num in buf:
    bindo_su[num]+=1
res=[]
for i in range(51):
    if bindo_su[i]==i: 
        res.append(bindo_su[i])
if len(res)==0 and (0 in buf): print(-1)
elif sum(res)==0: print(0)
else: print(max(res))