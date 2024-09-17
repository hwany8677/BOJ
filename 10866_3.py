#이게...왜...돌지?
#?????
#나만어렵게풀었어...
from sys import stdin
input=stdin.readline

buf=[]
length=0
for _ in range(int(input())):
    s=input().rstrip().split()
    if len(s)==2: cmd,x=s[0],int(s[1])
    else: cmd=s[0]
    if cmd=="push_front": 
        buf.insert(0,x)
        length+=1
    if cmd=="push_back":
        buf.append(x)
        length+=1
    if cmd=="pop_front": 
        if length<1: print(-1)
        else: 
            print(buf.pop(0))
            length-=1
    if cmd=="pop_back": 
        if length<1: print(-1)
        else: 
            print(buf.pop(length-1))
            length-=1
    if cmd=="size": print(length)
    if cmd=="empty": print(0 if length else 1)
    if cmd=="front": print(buf[0] if length else -1)
    if cmd=="back": print(buf[length-1] if length else -1)