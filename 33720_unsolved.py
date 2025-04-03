#3,5,7,11,13,17,19,23,29,31,37,41,...
prime=[i for i in range(0,1000000+1)]
for i in range(2,1000000+1):
    cnt=0
    if prime[i]==0: continue
    for j in range(i+i,1000000+1,i):
        if prime[j]%i==0: 
            prime[j]=0
            cnt+=1
prime=sorted(set(prime))
prime.remove(0)
prime.remove(1)
n=int(input())
if n%2==0: print(n//2)
else:
    min=1
    for element in prime:
        if n%element==0: min=element
        if n<element: break
    print(n//min)