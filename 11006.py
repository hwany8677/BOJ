for _ in range(int(input())):
    n,m=map(int,input().split())
    t=n//2
    m-=t
    n-=2*t
    u=n
    m-=n
    while(m>0):
        t-=1
        u+=2
        m-=1
    print(u,t)