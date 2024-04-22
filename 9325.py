t=int(input())
for i in range(0,t):
    s=int(input())
    n=int(input())
    part=[]
    for j in range(0,n):
        q,p=map(int,input().split())
        part.append(q*p)
    print(s+sum(part))