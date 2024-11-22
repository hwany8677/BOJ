from math import sqrt,floor
input=open(0).readline
prime=[True]*(1000003+1)
for i in range(2,floor(sqrt(1000003))+1):
    cnt=0
    if prime[i]==False: continue
    for j in range(i+i,1000003+1,i):
        if j%i==0: 
            prime[j]=False
            cnt+=1
prime[0]=False
prime[1]=False
for _ in range(int(input())):
    buf=list(map(int,input().split()))
    sigma=0
    for num in buf:
        init=num
        for i in range(init,1000004):
            if prime[i]: sigma+=i; break
    print(sigma)