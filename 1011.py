#산만함 MAX
#1~46342까지의 모든 경우를 따진다
#46341^2, 46341*46342
#이진 탐색
input=open(0).readline
buf=[i**2 for i in range(1,46343)]
buf2=[i*(i+1) for i in range(1,46344)]
final=[0]
final+=buf; final+=buf2
final.sort()
for _ in range(int(input())):
    x,y=map(int,input().split())
    dist=y-x
    low,high=1,92685 #ㅅㅂ 92685를 46343이라 적어놓고선 왜 틀렸는지 하루종일 고민함
    res=0
    while(1):
        mid=(low+high)//2
        if dist==final[mid]:
            res=mid
            break
        if low+1==high:
            res=low+1
            break
        if final[mid]<dist: low=mid
        elif dist<final[mid]: high=mid
    print(res)
