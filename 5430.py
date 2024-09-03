#1904ms is a disgrace :((((
from sys import stdin
input=stdin.readline

for _ in range(int(input())):
    p=input()
    n=input()
    buf=input()
    if buf=="[]\n": buf=[]
    else: buf=list(map(int,buf.strip('[').strip(']\n').split(',')))
    #reverse 메소드는 O(n) -> 끝부분을 정하고 pop 써야됨
    to_pop=0
    broken=False
    for cmd in p:
        if cmd=='R': 
            to_pop=0 if to_pop!=0 else len(buf)-1
        elif cmd=='D':
            try:
                buf.pop(to_pop)
                to_pop-=1 if to_pop!=0 else 0
            except IndexError:
                print("error")
                broken=True
                break
    if broken: continue
    if to_pop!=0: buf.reverse()
    print('[',end='')
    for i in range(len(buf)):
        print(buf[i],end='')
        if i<len(buf)-1: print(',',end='')
    print(']')
