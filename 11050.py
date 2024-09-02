n,k=map(int,input().split())
res=1
for i in range(1,n+1): res*=i
res_2=1
for i in range(1,k+1): res_2*=i
for i in range(1,n-k+1): res_2*=i
print(int(res/res_2))