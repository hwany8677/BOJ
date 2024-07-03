for k in range(int(input())):
    totalRev=0
    n,v=map(int,input().split())
    d,p=[0 for _ in range(n)],[0 for _ in range(n)]
    for i in range(n):
        #1: display 0: click
        d[i],p[i]=map(int,input().split())
    a1,a2=0,0
    c=0
    for _ in range(v):
        a1,a2,c=map(int,input().split())
        a1-=1; a2-=1
        #display ad
        totalRev+=p[a1] if d[a1] else 0
        totalRev+=p[a2] if d[a2] else 0
        #click ad
        totalRev+=p[a1] if d[a1]==0 and c==1 else 0
        totalRev+=p[a2] if d[a2]==0 and c==2 else 0
        # print(f"a1={a1} a2={a2} c={c}")
        # print(f"totalRev={totalRev}")
    print(f"Data Set {k+1}:\n{totalRev}\n")