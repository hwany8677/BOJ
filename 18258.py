#1. 굳이 pop을 할 필요 없고
#2. 굳이 len()을 중복으로 쓸 필요가 없다
from sys import stdin
input=stdin.readline

buf=[]
real_len=0
length=0
front=0
for _ in range(int(input())):
    s=input().rstrip().split()
    if len(s)==2: cmd,x=s[0],s[1]
    else: cmd=s[0]
    if cmd=="push": 
        buf.append(s[1])
        length+=1
        real_len+=1
    if cmd=="pop":
        if length==0: print(-1)
        else:
            print(buf[front])
            front+=1
            length-=1
    if cmd=="empty": print(0 if length else 1)
    if cmd=="size": print(length)
    if cmd=="front": 
        if length==0: print(-1)
        else: print(buf[front])
    if cmd=="back": 
        if length==0: print(-1)
        else: print(buf[real_len-1])