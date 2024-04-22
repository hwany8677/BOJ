n=int(input())
went=False
j=1
for i in range(0,2*n-1):
    if i==(2*n-1)//2: went=True
    if not(went):
        print("*"*j)
        j+=1
    else: 
        print("*"*j)
        j-=1