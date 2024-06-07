#d: light-year
#v: top light-year/h, f: fuel, c: fuel/h
#나눗셈때문에 지연이좀있는
for _ in range(int(input())):
    n,d=map(int,input().split())
    count=0
    for _ in range(n):
        v,f,c=map(int,input().split())
        if (f/c)*v>=d: count+=1
    print(count)