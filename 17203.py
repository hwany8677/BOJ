from sys import stdin
input=stdin.readline
def delta(lisT):
    res=[]
    for i in range(1,len(lisT)):
        res.append(abs(lisT[i]-lisT[i-1]))
    if len(res)==0: res=[0] #Remedy
    return res
def Sn(lisT):
    res=[lisT[0]]
    for i in range(1,len(lisT)):
        res.append(lisT[i]+res[i-1])
    return res
n,q=map(int,input().split())
buf=list(map(int,input().split()))
S=delta(buf)
S=Sn(S)
for _ in range(q):
    start,end=map(int,input().split())
    if start==end: print(0)
    elif start==1: print(S[end-2])
    else: print(S[end-2]-S[start-2])