#No list
n=int(input())
for i in range(0,n):
    for j in range(1 if i%2==0 else 0,n*2+1):
        if (j+1)%2==0: print("*",end='')
        else: print(" ",end='')
    print()