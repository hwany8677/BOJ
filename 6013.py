#Farthest points
#Just brute force the way
from sys import stdin
input=stdin.readline

n=int(input())
#For 8, 8C2=28 combinations required
cow_x,cow_y=[],[]
for _ in range(n):
    buf_x,buf_y=map(int,input().split())
    cow_x.append(buf_x)
    cow_y.append(buf_y)
mx=0
mx_pos1,mx_pos2=0,0
for i in range(n):
    for j in range(i+1,n):
        dist=(cow_x[i]-cow_x[j])**2+(cow_y[i]-cow_y[j])**2
        if dist>mx:
            mx=dist
            mx_pos1,mx_pos2=i,j
print(mx_pos1+1,mx_pos2+1)
