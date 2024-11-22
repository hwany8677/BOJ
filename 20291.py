input=open(0).readline
n=int(input())
ext=dict()
for _ in range(n):
    buf=input().rstrip().split('.')[1]
    if buf not in ext: ext[buf]=1
    else: ext[buf]+=1
value=ext.values()
ext=ext.keys()
zipped=list(zip(value,ext))
zipped.sort(key=lambda x:x[1])
for element in zipped: print(element[1],element[0])