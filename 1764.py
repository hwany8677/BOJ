from sys import stdin
input=stdin.readline
buf=[]
n,m=map(int,input().split())
for _ in range(n):
    s=input().rstrip()
    buf.append(s)
for _ in range(m):
    s=input().rstrip()
    buf.append(s)
buf.sort()
length=len(buf)
res=[]
count=0
for i in range(length):
    if i<length-1 and buf[i]==buf[i+1]:
        res.append(buf[i])
        count+=1
        i+=1
    else: continue
print(count)
for name in res: print(name)
