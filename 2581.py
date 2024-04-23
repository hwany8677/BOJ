#에라토스테네스의 채
from math import floor,sqrt
m=int(input())
n=int(input())
min=0
prime=[i for i in range(m,n+1)]
if prime[0]==1: prime[0]=0 #1은 소수가아님
for i in range(2,floor(sqrt(n))+1): #처음부터 2~n까지 있다고 가정
    for j in range(0,len(prime)):
        if prime[j]==0: 
            continue #2,4,6,... and 3,6,9,... replaced by 0->continue
        if prime[j]%i==0 and prime[j]!=i: 
            prime[j]=0
            continue #6->0->continue
for i in range(0,len(prime)):
    if prime[i]!=0: 
        min=prime[i]
        break
if min:
#   print(prime)
    print(sum(prime))
    print(min)
else: print(-1)