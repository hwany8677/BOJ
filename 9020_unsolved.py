def trace(nOriginal):
    n=nOriginal
    firstPrime=-1
    while(1):
        for i in range(n,1,-1):
            if sieve[i]==False: continue
            if firstPrime==-1: firstPrime=i
            n-=sieve[i]
        if n<0: 
            n=sieve[firstPrime]+1
            firstPrime=-1
from math import floor,sqrt
global sieve
sieve=[i for i in range(0,10000)]
for i in range(2,floor(sqrt(10000))+1):
    if sieve[i]==0: continue
    for j in range(i+i,10000,i):
        if sieve[j]%i==0:
            sieve[j]=0
for _ in range(int(input())):
    n=int(input())
    if n<4: continue
    