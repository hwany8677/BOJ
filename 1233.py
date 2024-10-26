#Naive works best
s1,s2,s3=map(int,input().split())
sums=[0 for _ in range(81)]
for i in range(1,s1+1):
    for j in range(1,s2+1):
        for k in range(1,s3+1):
            res=i+j+k
            sums[res]+=1
print(sums.index(max(sums)))
