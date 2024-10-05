#stdin.readline을 안쓰면 tle뜨는
from sys import stdin
input=stdin.readline

buf=[2147483648]
length=0
for _ in range(int(input())):
    x=int(input())
    if x==0:
        if length==0: print(0)
        else:
            print(buf[1])
            buf[1]=buf[length]
            buf.pop(length)
            length-=1
            if length==0: continue

            i=1
            while(i*2<length):
                ances=i
                where=i*2 if buf[i*2]>buf[(i*2)+1] else (i*2)+1
                if buf[ances]<=buf[where]: buf[ances],buf[where]=buf[where],buf[ances]
                i=where
            temp=length//2
            if buf[temp]<=buf[length]: buf[temp],buf[length]=buf[length],buf[temp]
    else: 
        if length==0:
            buf.append(x)
            length+=1
        else:
            buf.append(x)
            length+=1
            ances=length//2
            element=length
            while (ances>0): #상위 노드와 비교, 스왑
                if buf[ances]<=buf[element]: buf[ances],buf[element]=buf[element],buf[ances]
                ances//=2
                element//=2