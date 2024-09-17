#collections? deque? append? pop? 먹는 건가요?
#front: 왼쪽, back: 오른쪽
from sys import stdin
input=stdin.readline

deq=[0 for _ in range(20000)]
front=10001
back=9999
for _ in range(int(input())):
    s=input().rstrip().split()
    if len(s)==2: cmd,x=s[0],int(s[1])
    else: cmd=s[0]
    if cmd=="push_front":
        deq[front-1]=x
        #In case of deque contains nothing
        if front>back: 
            front-=1
            back+=1
        else: front-=1
    if cmd=="push_back":
        deq[back+1]=x
        if front>back: 
            front-=1
            back+=1
        else: back+=1
    if cmd=="pop_front":
        if front>back: print(-1)
        else:
            print(deq[front])
            deq[front]=0
            if front==back:
                front+=1
                back-=1
            else: front+=1
    if cmd=="pop_back":
        if front>back: print(-1)
        else: 
            print(deq[back])
            deq[back]=0
            if front==back:
                front+=1
                back-=1
            else: back-=1
    if cmd=="size": print(0 if front>back else back-front+1)
    if cmd=="empty": print(1 if front>back else 0)
    if cmd=="front": print(-1 if front>back else deq[front])
    if cmd=="back": print(-1 if front>back else deq[back])