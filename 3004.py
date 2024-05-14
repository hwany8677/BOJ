n=int(input())
if n==1:
    print(2)
else:
    x,y=2,2
    for i in range(2,n):
        if i%2==0: x+=1
        else: y+=1
    print(x*y)