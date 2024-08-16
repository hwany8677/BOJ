from sys import stdin
input=stdin.readline
#미리 안넣는 버전
from math import floor,sqrt
prime=[i for i in range(0,1009+1)]
for i in range(2,floor(sqrt(1009))+1):
    cnt=0
    if prime[i]==0: continue
    for j in range(i+i,1009+1,i): 
        if prime[j]%i==0: 
            prime[j]=0
            cnt+=1
prime=sorted(set(prime))
prime.remove(0)
prime.remove(1)
for _ in range(int(input())):
    k=int(input())
    sigma=0
    mx=0
    while(prime[mx]<k):
        if prime[mx]<k: mx+=1
    mx=prime[mx-1]
    foundPair=False
    for a in prime:
        if a>mx: break
        
        for b in prime:
            if b>mx: break
            
            for c in prime:
                if c>mx: break
                res=a+b+c
                if res==k: 
                    foundPair=True
                    break
            
            if foundPair: break
        
        if foundPair: break
    if not(foundPair): print(0)
    else: print(a,b,c)