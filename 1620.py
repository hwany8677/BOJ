from sys import stdin
input=stdin.readline

buf2=dict()
n,m=map(int,input().split())
buf=[]
for i in range(1,n+1): 
    s=input().rstrip()
    buf.append(s)
    buf2[s]=i
for _ in range(m):
    s=input().rstrip()
    orded=ord(s[0])
    if orded>48 and orded<58: 
        s=int(s)
        print(buf[s-1])
    else: print(buf2[s])