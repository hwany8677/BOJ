input=open(0).readline
n,s=map(int,input().split())
buf=[]
for _ in range(n): buf.append(int(input()))
count=0
for i in range(n):
    for j in range(i+1,n):
        a,b=buf[i],buf[j]
        if a+b<=s: count+=1
print(count)