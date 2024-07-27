#Is sum() O(n)?
from sys import stdin
input=stdin.readline
def Sn(lisT):
    res=[lisT[0]]
    for i in range(1,len(lisT)):
        res.append(lisT[i]+res[i-1])
    return res
sigma=[]
for _ in range(int(input())):
    buf=list(map(int,input().split()))
    buf.pop(0)
    sigma.append(sum(buf))
sigma.sort()
S=Sn(sigma)
print(sum(S))