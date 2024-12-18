input=open(0).readline
for _ in range(int(input())):
    n=int(input())
    candy=list(map(int,input().split()))
    cycles=0
    while(1):
        if cycles==0: #머리아프게 생각ㄴ
            for i in range(n):
                if candy[i]%2: candy[i]+=1
            candies=candy[0]
            verified=1
            for i in range(1,n):
                amount=candy[i]
                if amount==candies: verified+=1
            if verified==n: break
        #Cycling
        #생각하는 그대로를 코드로 적으면 끝임
        to_add=[]
        for i in range(-1,n-1): to_add.append(candy[i]//2)
        for i in range(n): 
            candy[i]//=2
            candy[i]+=to_add[i]
        #Supplement
        for i in range(n):
            if candy[i]%2: candy[i]+=1
        cycles+=1
        #Verification
        candies=candy[0]
        verified=1
        for i in range(1,n):
            amount=candy[i]
            if amount==candies: verified+=1
        if verified==n: break
    print(cycles)