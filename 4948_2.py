#'제대로 된' 에라토스테네스를 가져왔다!
from math import floor,sqrt
sieve=[i for i in range(0,246913)]
for i in range(2,floor(sqrt(246912))+1):
    if sieve[i]==0: continue
    for j in range(i+i,246913,i):
        if sieve[j]%i==0:
            sieve[j]=0
while(1):
    n=int(input())
    if n==0: break
    c=0
    for i in range(n+1,2*n+1):
        if sieve[i]!=0: c+=1
    print(c)