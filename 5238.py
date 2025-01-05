input=open(0).readline
for _ in range(int(input())):
    buf=list(map(int,input().split()))
    is_fibo=True
    for i in range(3,len(buf)):
        a,b=buf[i-2],buf[i-1]
        if buf[i]==(a+b): continue
        else: is_fibo=False
    print("YES" if is_fibo else "NO")