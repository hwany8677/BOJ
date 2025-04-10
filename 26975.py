#이익을 maxing
#여러 답안이 있으므로 완전탐색 해야만 함 (짜피2초임)
#큰 애들부터 시작
n=int(input())
c=list(map(int,input().split()))
if n==1:
    print(c[0],c[0])
    exit(0)
c.sort()
i=n-1
mn=c[i]
sigma,sigma_final=0,0
while(i>=0):
    while(c[i]==c[i-1] and i>0): i-=1
    sigma=c[i]*(n-i)
    #print(f"sigma={sigma}={c[i]}*{n-i}, i={i}, c[i]={c[i]}")
    if sigma>=sigma_final:
        if c[i]<mn:
            mn=c[i]
            #print(mn)
        sigma_final=sigma
        #print(f"sigma_final={sigma_final}")
    i-=1
print(sigma_final,mn)
