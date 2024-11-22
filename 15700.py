n,m=map(int,input().split())
if n<2 and m<2: print(0); exit(0)
if n==1: print(m//2)
elif m==1: print(n//2)
else:
    if m%2: print((m//2)*n+(n//2))
    else: print((m//2)*n)