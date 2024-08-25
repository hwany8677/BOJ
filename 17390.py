from sys import stdin
input=stdin.readline

def Sn(lisT):
    res=[lisT[0]]
    for i in range(1,len(lisT)):
        res.append(lisT[i]+res[i-1])
    return res
n,q=map(int,input().split())
buf=sorted(list(map(int,input().split())))
s=Sn(buf)
for _ in range(q):
    start,end=map(int,input().split())
    print(s[end-1]-s[start-2] if start>1 else s[end-1])