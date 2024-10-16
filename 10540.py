input=open(0).readline
x,y=[],[]
for _ in range(int(input())):
    a,b=map(int,input().split())
    x.append(a); y.append(b)
dx=max(x)-min(x)
dy=max(y)-min(y)
print(dx**2 if dx>dy else dy**2)
