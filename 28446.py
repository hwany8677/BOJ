input=open(0).readline
ball=dict()
for _ in range(int(input())):
    buf=input().rstrip().split()
    if len(buf)==3:
        req=buf[0]
        x,w=int(buf[1]),int(buf[2])
        ball[w]=x
    else:
        req=buf[0]
        w=int(buf[1])
        print(ball[w])