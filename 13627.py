input=open(0).readline
n,r=map(int,input().split())
buf=[i for i in range(1,n+1)]
returned=list(map(int,input().split()))
returned.sort()
for ret in returned: buf.remove(ret)
if n==r: print("*")
else: print(*buf)
