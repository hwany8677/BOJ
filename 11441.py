from sys import stdin
input=stdin.readline

def Sn(lisT):
    res=[lisT[0]]
    for i in range(1,len(lisT)):
        res.append(lisT[i]+res[i-1])
    return res
input()
buf=list(map(int,input().split()))
s=Sn(buf)
n=int(input())
for _ in range(n):
    start,end=map(int,input().split())
    print(s[end-1]-s[start-2] if start>1 else s[end-1])