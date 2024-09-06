from sys import stdin
input=stdin.readline

coord=[[] for _ in range(200001)]
for _ in range(int(input())):
    x,y=map(int,input().split())
    y+=100000
    coord[y].append(x)
for i in range(200001):
    if len(coord[i])==0: continue
    coord[i].sort()
    for j in range(len(coord[i])):
        print(coord[i][j],i-100000)