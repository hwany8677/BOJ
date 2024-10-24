input=open(0).readline
flip=False
time=1
for _ in range(int(input())):
    buf=input().split()
    card=buf[0]
    x=int(buf[1])
    if card=='HOURGLASS':
        if x!=time: flip=not(flip)
    print(time,"YES" if x==time and card!='HOURGLASS' else "NO")
    time=time-1 if flip else time+1
    if time==0: time=12
    elif time==13: time=1
