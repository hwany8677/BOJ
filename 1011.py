#산만함 MAX
#1~46342까지의 모든 경우를 따진다
#46341^2, 46341*46342
input=open(0).readline
for _ in range(int(input())):
    x,y=map(int,input().split())
    dist=y-x
    buf=[i**2 for i in range(1,46342)]
    buf2=[i*(i+1) for i in range(1,46343)]
    final=sorted(buf+buf2)
    #dist>final[i] 인 경우 바로 멈춤
    i=0
    while(1):
        if dist>final[i]:
            i-=1
            break
        i+=1
    print(final[i])