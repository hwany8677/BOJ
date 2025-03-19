input=open(0).readline
for _ in range(int(input())):
    buf=list(map(int,input().split()))
    prev=buf[0]
    sigma=0
    for i in range(1,len(buf)):
        if buf[i]>prev*2: sigma+=(buf[i]-prev*2)
        prev=buf[i]
    print(sigma)
