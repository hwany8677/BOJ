input=open(0).readline
for _ in range(int(input())):
    a,b=map(int,input().split())
    x=a;y=a;i=a
    doesExist=0
    while(x+y<=b):
        if x+y==b: 
            doesExist=1
            break
        y=a*(i+1)
        if x+y==b:
            doesExist=1
            break
        x=a*(i+1)
        i+=1
    print(doesExist)