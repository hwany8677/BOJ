#현재 많은 곳에서 많아야 할 곳으로 빼낸다
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
count=0
for i in range(n):
    temp=a[i]-b[i]
    if temp<0: continue
    else: count+=temp
print(count)