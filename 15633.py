n=int(input())
res=0
for i in range(1,n+1):
    if n%i==0: res+=i
res*=5
res-=24
print(res)