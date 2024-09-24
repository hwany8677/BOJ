from sys import stdin
input=stdin.readline
plane=[[0 for _ in range(100)] for _ in range(100)]
mx_x,mx_y=0,0
for _ in range(int(input())):
    x,y=map(int,input().split())
    if x+10>mx_x: mx_x=x+10
    if y+10>mx_y: mx_y=y+10
    x-=1; y-=1
    for i in range(y,y+10):
        for j in range(x,x+10): plane[i][j]=True
sigma=0
for i in range(mx_y):
    for j in range(mx_x): sigma+=plane[i][j]
print(sigma)
