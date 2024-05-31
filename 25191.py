n=int(input())
a,b=map(int,input().split())
e=0
while(n>0):
    if (a>1): 
        a-=2
        e+=1
    elif (b>0):
        b-=1
        e+=1
    n-=1
print(e)