from sys import stdin
input=stdin.readline
def Sn(lisT):
    res=[lisT[0]]
    for i in range(1,len(lisT)):
        res.append(lisT[i]+res[i-1])
    return res
n,m=map(int,input().split())
buf=list(map(int,input().split()))
s=Sn(buf)
count=0
start,end=0,n-1
while(end<n):
    if start==0: sigma=s[start]
    else: sigma=s[end]-s[start-1]
    if sigma==m: count+=1
    start+=1
    end+=1
print(count)