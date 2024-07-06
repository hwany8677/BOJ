#수학은 말이에요 참 신기한 거에요
# from time import process_time as p
from sys import stdin
def Sn(buf,length):
    S=[buf[0]]
    for k in range(1,length):
        S.append(buf[k]+S[k-1])
    return S
n,m=map(int,input().split())
buf=list(map(int,input().split()))
# t0=p()
S=Sn(buf,n)
# t=p()
# print(f"List gen took {t-t0} seconds")
for _ in range(m):
    i,j=map(int,stdin.readline().split())
    if i==1: print(S[j-1])
    else: print(S[j-1]-S[i-2])