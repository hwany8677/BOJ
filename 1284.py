#0: 4cm, 1: 2cm, other: 3cm
input=open(0).readline
n=int(input())
sigma=2
while(n!=0):
    for digit in str(n):
        if digit=='0': sigma+=4
        elif digit=='1': sigma+=2
        else: sigma+=3
    sigma+=len(str(n))-1
    print(sigma)
    n=int(input())
    sigma=2
