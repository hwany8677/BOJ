#조합론? Naga. (I,V,X,L)
from math import factorial as fact
n=int(input())
precalc=[0,4,10,20,35
if n<5:
    sigma=0
    for i in range(1,n+1): sigma+=fact(4)//(fact(n)*fact(4-n))
    print(sigma)