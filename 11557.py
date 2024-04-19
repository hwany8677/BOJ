t=int(input())
sc=[]
lq=[]
max=0
for i in range(0,t):
    n=int(input())
    for j in range(0,n):
        s,l=input().split()
        l=int(l)
        sc.append(s)
        lq.append(l)
        if lq[j]>lq[max]: max=j
    print(sc[max])