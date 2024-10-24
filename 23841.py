input=open(0).readline
n,m=map(int,input().split())
for _ in range(n):
    buf=list(input().rstrip())
    length=len(buf)
    for i in range(length//2):
        if buf[i].isalpha(): buf[length-1-i]=buf[i]
        elif buf[length-1-i].isalpha(): buf[i]=buf[length-1-i]
    print(*buf,sep='')
