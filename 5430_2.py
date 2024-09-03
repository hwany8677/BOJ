#OPTIMIZINGGGG
#Got 396ms using w/o pop method
from sys import stdin
input=stdin.readline

for _ in range(int(input())):
    p=input()
    n=int(input())
    buf=input()
    if buf=="[]\n": buf=[]
    else: 
        buf=buf.split(',')
        buf[0]=buf[0].strip('[')
        buf[n-1]=buf[n-1].strip(']\n')
    to_pop=0 #0: left, 1: right
    broken=False
    start,end=0,n
    for cmd in p:
        if cmd=='R':
            to_pop=0 if to_pop!=0 else 1
        elif cmd=='D': 
            if to_pop: end-=1
            else: start+=1
            if start>end: 
                print("error")
                broken=True
                break
    if broken: continue
    if to_pop: rangE=range(end-1,start-1,-1)
    else: rangE=range(start,end)
    print('[',end='')
    for i in rangE:
        print(buf[i],end='')
        if i<end-1 and not(to_pop): print(',',end='')
        elif i>start and to_pop: print(',',end='')
    print(']')