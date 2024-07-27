n=int(input())
buf=[]
pos=0
for i in range(n):
    temp=input()
    if temp=='?': pos=i
    buf.append(temp)
if pos==0 and len(buf)==1: #1 / ?
    n=int(input())
    for _ in range(n-1): input()
    res=input()
elif pos==0: # ? 단어2 단어3
    end=buf[pos+1][0]
    n=int(input())
    for _ in range(n):
        s=input()
        if s[len(s)-1]==end:
            if s in buf: continue
            res=s
elif pos==len(buf)-1: # 단어1 단어2 ?
    start=buf[pos-1][len(buf[pos-1])-1]
    n=int(input())
    for _ in range(n):
        s=input()
        if s[0]==start:
            if s in buf: continue
            res=s
else: # 단어1 ? 단어3
    n=int(input())
    start,end=buf[pos-1][len(buf[pos-1])-1],buf[pos+1][0]
    for _ in range(n):
        s=input()
        if s[0]==start and s[len(s)-1]==end:
            if s in buf: continue
            res=s
print(res)