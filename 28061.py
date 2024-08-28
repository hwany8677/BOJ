n=int(input())
buf=list(map(int,input().split()))
mx=0
for i in range(n):
    if buf[i]-(n-i)>=mx: mx=buf[i]-(n-i)
print(mx)