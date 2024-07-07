def theGreatAndPowerfulDivisor(a,b):
    r=a%b
    while(r!=0):
        a=b
        b=r
        r=a%b
    return b
n,m=map(int,input().split(":"))
gcd=theGreatAndPowerfulDivisor(n,m) if n>=m else theGreatAndPowerfulDivisor(m,n)
n//=gcd
m//=gcd
print(n,m,sep=':')