input=open(0).readline
n,m=map(int,input().split())
count=0
for _ in range(n):
    op=input().rstrip()
    o=0
    for c in op:
        if c=='O': o+=1
    if o>=m/2: count+=1
print(count)
