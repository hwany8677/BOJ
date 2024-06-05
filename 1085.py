#점에서 변까지의 최단거리 -> 대각선이 아님.
x,y,w,h=map(int,input().split())
d=[x,y,w-x,h-y]
print(min(d))