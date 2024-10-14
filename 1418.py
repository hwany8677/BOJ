#하...이게 뭐라고 오래 걸일 일인가...ㅠㅠ
from math import sqrt,floor
sieve=[i for i in range(102)]
for i in range(2, floor(sqrt(102))+1):
    if sieve==[0]: continue
    for j in range(i+i,102,i):
        if sieve[j]%i==0:
            sieve[j]=0
sieve=sorted(set(sieve))
sieve.remove(0); sieve.remove(1)
n=int(input())
k=int(input())
count=1
for i in range(2,n+1):
    junsu=True
    divided=False
    j=0
    i_copy=i
    while(j<len(sieve)):
        if i_copy%sieve[j]==0:
            if sieve[j]>k:
                junsu=False
                break
            else: i_copy//=sieve[j]
        else: j+=1
    if junsu and i_copy==1: count+=1
print(count)
