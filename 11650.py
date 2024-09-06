#coord[0] == x=-100,000
#coord[200000] == x=100,000
#os.read()?
from sys import stdin
input=stdin.readline

coord=[[] for _ in range(200001)]
for _ in range(int(input())):
    x,y=map(int,input().split())
    x+=100000
    coord[x].append(y)
for i in range(200001):
    if len(coord[i])==0: continue
    coord[i].sort()
    for j in range(len(coord[i])):
        print(i-100000,coord[i][j])