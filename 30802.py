n=int(input())
buf=list(map(int,input().split()))
t,p=map(int,input().split())
ts_count=0
for size_c in buf:
    if size_c%t==0: temp=size_c//t
    else: temp=(size_c//t)+1
    ts_count+=temp
print(ts_count)
print(n//p,n%p)