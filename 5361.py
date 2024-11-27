input=open(0).readline
a,b,c,d,e=350.34,230.90,190.55,125.30,180.90
for _ in range(int(input())):
    A,B,C,D,E=map(int,input().split())
    sigma="{:.2f}".format(a*A+b*B+c*C+d*D+e*E)
    print(f"${sigma}")
