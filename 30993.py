from math import factorial
f=factorial
n,a,b,c=map(int,input().split())
count=1
count*=f(n)//( f(c)*f(n-c) )
n-=c
count*=f(n)//( f(b)*f(n-b) )
n-=b
count*=f(n)//( f(a)*f(n-a) )
print(count)