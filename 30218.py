#1a+2b+3c
#-> 1b+2c+3d를 할려면
#1a+2b+3c - (a+b+c) + 3d를 해야하고
#
#1c+2d+3e를 할려면
#1b+2c+3d - (b+c+d) + 3e를 해야한다
#=> 애초에 식 정리를 해야되는 문제
from sys import stdin
from collections import deque
input=stdin.readline

def Sn(lisT):
    res=[lisT[0]]
    for i in range(1,len(lisT)):
        res.append(lisT[i]+res[i-1])
    return res

def Sn_final(lisT,size):
    global c_sum
    res=[]
    sigma=0
    for i in range(len(lisT)-size):
        left=i
        right=i-len(lisT)+1
        sigma-=c_sum[right]-c_sum[left-1]
        sigma+=size*lisT[right+1]
        res.append(sigma)
    return res

n,k=map(int,input().split())
buf=[]
for _ in range(n): buf.append(int(input()))
c_sum=Sn(buf)
s=Sn_final(buf,k)
s.sort()
for i in range(len(s)):
    print(s[i][1],s[i][0])