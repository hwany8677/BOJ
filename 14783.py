n,l=map(int,input().split())
snipe=list(map(int,input().split()))
cows=[i for i in range(1,n+1)]
i=0
step=snipe[0]
turn=0
killed=0
while(1):
    step=snipe[turn]
    while(step>0):
        if cows[i]==0: i+=1
        elif cows[i]!=0: 
            i+=1
            step-=1
        if i==n: i=0
        if sum(cows)==0: break
    if sum(cows)==0: break
    killed=cows[i-1]
    # print(killed)
    cows[i-1]=0
    turn+=1
    if turn==l: turn=0
print(killed)