from sys import stdin
input=stdin.readline
# (1) 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다. = 2초
# (2) 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다. = 1초
#*** 집터 내에서 블록을 가져올 수 있음 ***
#-> 이때 걸리는 시간 = 3초
n,m,b=map(int,input().split()) #b: 인벤에 있는 블록개수
land=[]
# n m ------->
# |
# |
# |
# v
for _ in range(n): land.append(list(map(int,input().split())))
#1. 다 캔다
#2. 다 채운다
