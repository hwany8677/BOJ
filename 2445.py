#2523 + 2533 = 2445
#공백 개수: 짝수
n=int(input())
went=False
j=1
for i in range(0,2*n-1):
    if i==(2*n-1)//2: went=True
    if not(went):
        print("*"*j,end='')
        print(" "*(2*(n-j)),end='')
        print("*"*j)
        j+=1
    else: 
        print("*"*j,end='')
        print(" "*(2*(n-j)),end='')
        print("*"*j)
        j-=1