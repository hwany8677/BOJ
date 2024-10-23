n,k=map(int,input().split())
buf=list(map(int,input().split()))
start,end=0,k-1
sigma=0
for i in range(k): sigma+=buf[i]
mx=sigma
while(end<n-1):
    sigma-=buf[start]
    sigma+=buf[end+1]
    if sigma>mx: mx=sigma
    start+=1
    end+=1
print(mx)