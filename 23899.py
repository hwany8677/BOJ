n=int(input())
buf=list(map(int,input().split()))
desired=list(map(int,input().split()))
match=False
if buf==desired: print(1); exit(0)
for i in range(n-1,0,-1):
    mx,mx_idx=buf[i],0
    for j in range(i):
        if buf[j]>buf[i] and buf[j]>mx: mx,mx_idx=buf[j],j
    if mx>buf[i]: buf[i],buf[mx_idx]=buf[mx_idx],buf[i]
    if buf==desired: match=True
print(int(match))