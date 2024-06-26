from math import floor,sqrt
sieve=[i for i in range(0,104)]
for i in range(2,floor(sqrt(104))+1):
    if sieve[i]==0: continue
    for j in range(i+i,104,i):
        if sieve[j]%i==0:
            sieve[j]=0
sieve[0],sieve[1]=0,0
sieve=sorted(set(sieve))
sieve.remove(0)
special_yr=[]
for i in range(1,len(sieve)): special_yr.append(sieve[i-1]*sieve[i])
special_yr=sorted(set(special_yr))
n=int(input())
for yr in special_yr:
    if yr>n: 
        print(yr)
        exit(0)