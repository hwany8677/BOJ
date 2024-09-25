n=int(input())
buf=list(map(int,input().split()))
b,c=map(int,input().split())
sigma=0
for a_i in buf:
    if a_i<=b: sigma+=1; continue
    temp=a_i
    temp-=b
    sigma+=1
    while(1):
        if temp<=c: sigma+=1; break
        sigma+=temp//c
        temp-=(temp//c)*c
print(sigma)
