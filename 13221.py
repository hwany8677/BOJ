input=open(0).readline
wait_x,wait_y=map(int,input().split())
n=int(input())
mn=202
res_x,res_y=0,0
for _ in range(n):
    x,y=map(int,input().split())
    dist_x,dist_y=abs(wait_x-x),abs(wait_y-y)
    dist=dist_x+dist_y
    if dist<mn: mn,res_x,res_y=dist,x,y
print(res_x,res_y)