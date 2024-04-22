#2523번 코드에 덕지덕지
n=int(input())
went=False
j=1
s=n-1
for i in range(0,2*n-1):
    if i==(2*n-1)//2: went=True
    print(" "*abs(s),end='')
    if not(went):
        print("*"*j)
        j+=1
    else: 
        print("*"*j)
        j-=1
    s-=1