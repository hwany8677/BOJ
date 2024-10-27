from math import sqrt
input=open(0).readline
for _ in range(int(input())):
    s1=input().rstrip()
    x1,y1,z1=map(float,input().split())
    s2=input().rstrip()
    x2,y2,z2=map(float,input().split())
    res=(x2-x1)**2+(y2-y1)**2+(z2-z1)**2
    print(s1,"to",s2+':',"{:.2f}".format(sqrt(res)))
