from sys import stdin
input=stdin.readline

def order(od, s):
    zp=zip(s, od)
    res=[x for _, x in sorted(zp)]
    return res

n,k=map(int,input().split())
buf=[]
od=[i+1 for i in range(n-k+1)]
for _ in range(n): buf.append(int(input()))
sigma=sum(buf)
sigma_list=[sigma*i for i in range(1,k+1)]