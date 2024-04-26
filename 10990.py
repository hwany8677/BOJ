#거꾸로와 홀수의 조화
n=int(input())
for i in range(0,n):
    print(" "*(n-i-1),end='')
    print("*",end='')
    print(" "*(2*i-1),end='')
    print("*" if i!=0 else "")