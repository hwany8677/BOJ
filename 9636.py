#Minimum possible = 무조건 제3사분면 방면으로.
#Maximum possible = 무조건 제1사분면 방면으로.
input=open(0).readline
for _ in range(int(input())):
    x,y=0,0
    command=input().rstrip()
    minx,miny,maxx,maxy=0,0,0,0
    for cmd in command:
        if cmd=='U': miny+=1; maxy+=1
        if cmd=='D': miny-=1; maxy-=1
        if cmd=='L': minx-=1; maxx-=1
        if cmd=='R': minx+=1; maxx+=1
        if cmd=='?':
            minx-=1; miny-=1
            maxx+=1; maxy+=1
    print(minx,miny,maxx,maxy)
