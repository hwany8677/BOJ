#관찰이 필요한 문제
from math import log2
n=int(input())
t=2**int(log2(n))
if (t==n):
    print(t)
else:
    temp=n-t
    print(2*temp)