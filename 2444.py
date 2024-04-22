ps_n=int(input())
n=1
pastCenter=False
c=0
for i in range(0,2*ps_n-1):
    for j in range(1,ps_n-c): print(" ",end='')
    for k in range(0,n): print("*", end='')
    print()
    if n==2*ps_n-1: pastCenter=True
    if pastCenter: 
        n-=2
        c-=1
    else: 
        n+=2
        c+=1