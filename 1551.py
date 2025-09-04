n,k=map(int,input().split())
buf=list(map(int,input().split(",")))
for _ in range(k):
    for i in range(n-1):
        buf[i]=buf[i+1]-buf[i]
    n-=1
for idx in range(n): print(f"{buf[idx]}," if idx<n-1 else buf[idx],end='')
print()
