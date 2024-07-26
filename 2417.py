from math import sqrt
n=int(input())
res=int(sqrt(n))
if (res**2<n): res+=1
print(res)
