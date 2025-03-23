input=open(0).readline
b,n,m=map(int,input().split())
items=dict()
for _ in range(n):
    i,p=input().rstrip().split()
    items[i]=int(p)
total=0
for _ in range(m): total+=items[input().rstrip()]
if total<=b: print("acceptable")
else: print("unacceptable")