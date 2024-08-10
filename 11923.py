#n^2 won't matter
n,c=map(int,input().split())
w=list(map(int,input().split()))
mx=0
for i in range(n):
    fruit_start=w[i]
    if fruit_start>=c: continue
    w_sigma=fruit_start
    f_count=1
    for j in range(i+1,n):
        if w_sigma+w[j]<=c: 
            w_sigma+=w[j]
            f_count+=1
        else: continue
    mx=f_count if f_count>mx else mx
print(mx)