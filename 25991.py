#4로 나누고 -> 세제곱하고 -> 다 더하고 -> 합을 세제곱근 하고 -> 4를 곱하기
from math import cbrt
n=int(input())
buf=list(map(float,input().split()))
for i in range(n): 
    buf[i]/=4
    buf[i]**=3
sigma=sum(buf)
sigma=cbrt(sigma)
sigma*=4
temp=str(sigma).split(".")
if temp[1]=='0': print(int(sigma))
else: print(sigma)