input=open(0).readline
n,m=map(int,input().split())
res=[0 for _ in range(m)]
idx=[i for i in range(1,m+1)]
for _ in range(n):
    buf=list(map(int,input().split()))
    for i in range(m):
        bit=buf[i]
        if bit: res[i]+=1
zipped=list(zip(idx,res))
zipped.sort(key=lambda x:x[1])
zipped.reverse()
final=[[] for _ in range(zipped[0][1])]
for element in zipped: final[element[1]-1].append(element[0])
final.reverse()
for lisT in final:
    lisT.sort()
    for element in lisT: print(element,end=' ')
print()
