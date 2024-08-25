#누적합풀이
def Sn(lisT):
    res=[lisT[0]]
    for i in range(1,len(lisT)):
        res.append(lisT[i]+res[i-1])
    return res
n,m=map(int,input().split())
buf=list(map(int,input().split()))
s=Sn(buf)
res=[]
for i in range(m-1,n):
    if i==m-1: res.append(s[i])
    else: res.append(s[i]-s[i-m])
print(max(res))