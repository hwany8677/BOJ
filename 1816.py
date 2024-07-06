#'만일 S의 모든 소인수가 10^6보다 크다면 그 수는 적절한 암호 키이고, 그렇지 않은 경우는 적절하지 못한 암호 키가 된다.'
#-> S의 모든 약수가 10^6보다 크면 된다! = 즉 S는 소수!
#2~1,000,000까지의 소인수가 있으면 안됨!! = 이 소인수들로 나누어떨어지면 낙방
from math import floor,sqrt
sieve=[i for i in range(0,1000001)]
for i in range(2,floor(sqrt(1000000))+1):
    if sieve[i]==0: continue
    for j in range(i+1,1000001,i):
        if j%i==0: 
            sieve[j]=0
sieve=sorted(set(sieve))
sieve.remove(0)
sieve.remove(1)
for _ in range(int(input())):
    s=int(input())
    isAdequate=True
    for number in sieve:
        if s%number==0: 
            isAdequate=False
            break
    print("YES" if isAdequate else "NO")