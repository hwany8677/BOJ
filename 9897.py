input=open(0).readline
l,g,r=map(int,input().split())
lamp=[0 for _ in range(l+1)] #0번은 항상 꺼져있음
guard=dict()
for _ in range(g):
    buf=input().rstrip().split()
    guard[buf[0]]=(int(buf[1]),int(buf[2]))
for _ in range(r):
    buf=input().rstrip()
    a0=guard[buf][0]
    d=guard[buf][1]
    while(a0<l+1):
        lamp[a0]=not(lamp[a0])
        a0+=d
count=0
for l in lamp:
    if l: count+=1
print(count)
