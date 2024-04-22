ps_n=int(input())
n=1
for i in range(0,ps_n):
    for j in range(1,ps_n-i): print(" ",end='')
    for k in range(0,n): print("*",end='')
    n+=2
    print()