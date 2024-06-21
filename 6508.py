#TLE~ TLE~ 신나는노래~
#나도함께~ 불러보자~
file=open("result.txt","w")
while(1):
    n=int(input())
    if n==0: break
    bowl=list(map(int,input().split()))
    count=0
    i=0
    while(sum(bowl)!=0):
        if bowl[i]==0:
            i=0
            continue
        if i==0: 
            bowl[i]-=1 if bowl[i]>0 else 0
            count+=1
        else:
            if bowl[i]>0:
                bowl[i]-=1
                for j in range(i): bowl[j]+=1
                count+=1
        i=i+1 if i+1<n else 0
        for j in range(n): file.write(str(bowl[j])+' ')
        file.write('\n')
    print(count)
file.close()