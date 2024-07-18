#거리는 시작점 및 끝점을 제외해야함 (단, 꺾이는 경우는 제외)
from sys import stdin
input=stdin.readline
start,end=map(int,input().split())
#몫과 나머지 -> 가로(x)과 세로(y)로 치환
#11 -> (2,1) 33 -> (8, 3)
startX,startY=(start//4)-1 if start%4==0 else start//4, (0 if start%4==0 else 4-start%4)
endX,endY=(end//4)-1 if end%4==0 else end//4, (0 if end%4==0 else 4-end%4)
dist=abs(endX-startX)+abs(endY-startY)
if startX==endX and startY==endY: dist=0
print(dist)