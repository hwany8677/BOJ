#Screw lambda functions
def product(lisT):
    pi=1
    for n in lisT: pi*=n
    return pi
n=int(input())
number=[]
pi=[]
sigma=[]
for i in range(n):
    buf=list(map(int,input().split()))
    number.append(buf[0])
    pi.append(product(buf[1:]))
    sigma.append(sum(buf[1:]))
    