from os import system
while(1):
    n=int(input())
    if n==0: break
    bowl=list(map(int,input().split()))
    count=0
    upOrDown=True #up: True down: False
    i=0
    while(sum(bowl)!=0):
        if i==0: bowl[i]-=1 if bowl[i]>0 else 0
        else:
            if bowl[i]>0:
                bowl[i]-=1
        count+=1
        print(*bowl)
        system("pause")
        i=i+1 if i+1<n else 0
        # i=i+1 if upOrDown else i-1
        # if i==n: i,upOrDown=i-2, False
        # elif i==-1: i,upOrDown=i+2, True
    print(count)
