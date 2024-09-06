real_n=int(input())
n=real_n
a,pa,b,pb=map(int,input().split())
#count가 곧 cost
res=[0,0]
count_a=(n//pa)
for c_a in range(count_a+1):
    count_b=((n-c_a*pa)//pb)
    if pa*c_a+pb*count_b<=n:
        res=[c_a,count_b]
count_b=(n//pb)
for c_b in range(count_b+1):
    count_a=((n-c_b*pb)//pa)
    if pb*c_b+pa*count_a<=n:
        res=[count_a,c_b]

print(res[0],res[1])