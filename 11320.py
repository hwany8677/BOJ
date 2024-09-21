#닮은비 a^2:b^2
from sys import stdin
input=stdin.readline

def gcd(a,b):
    q=a//b; r=a%b 
    while(r>0):
        if r==0: break
        a,b=b,r
        q=a//b; r=a%b 
    return b
for _ in range(int(input())):
    a,b=map(int,input().split())
    to_divide=gcd(a,b)
    a//=to_divide; b//=to_divide
    print(a**2)