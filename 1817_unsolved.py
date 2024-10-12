#그리디 시러
n,m=map(int,input().split())
if n==0: print(0); exit(0)
buf=list(map(int,input().split()))
buf.append(1001)
i=0
count=0
current=0
while(i<n):
    current+=buf[i]
    if current==n:
        count+=1
        current=0
    elif current+buf[i+1]>m:
        count+=1
        current=0
    i+=1
print(count)