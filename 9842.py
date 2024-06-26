from math import floor,sqrt
sieve=[i for i in range(0,150000)]
for i in range(2,floor(sqrt(150000))+1):
    if sieve[i]==0: continue
    for j in range(i+i,150000,i):
        if sieve[j]%i==0:
            sieve[j]=0
sieve[1]=0
sieve=sorted(set(sieve))
sieve.remove(0)
print(sieve[int(input())-1])