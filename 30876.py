input=open(0).readline
mn_x,mn_y=0,1001
for _ in range(int(input())):
    x,y=map(int,input().split())
    if y<mn_y: 
        mn_x=x
        mn_y=y
print(mn_x,mn_y)