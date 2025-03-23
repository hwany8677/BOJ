#정수론 again
#약수 찾기
#n=a^(x)*b^(y) 꼴 일때(a와 b는 소수) n의 약수 개수는 (x+1)(y+1)임을 이용
#sqrt(10^7).=.3162이므로 사실 전처리 해줘도 상관은 없음
sieve=[i for i in range(3163)]
for i in range(2,3163):
    if sieve[i]==0: continue
    for j in range(2*i,3163,i):
        if sieve[j]%i==0:
            sieve[j]=0
sieve=sorted(set(sieve))
sieve.remove(0)
sieve.remove(1)
for _ in range(int(input())):
    l,u=map(int,input().split())
    mx=0
    for num in range(l,u+1):
        
    print(mx)
