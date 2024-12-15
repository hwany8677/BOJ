#1: Player 1, 2: Player 2
input=open(0).readline
ttt=[[0 for _ in range(3)] for __ in range(3)]
turn=int(input())
for _ in range(9):
    x,y=map(int,input().split())
    if turn==1: 
        ttt[x-1][y-1]=1
        turn=2
    else: 
        ttt[x-1][y-1]=2
        turn=1
    #가로 check
    for i in range(3):
        ones,twos=0,0
        for j in range(3):
            current=ttt[i][j]
            if current==1: ones+=1
            elif current==2: twos+=1
        if ones==3: print(1); exit(0)
        elif twos==3: print(2); exit(0)
    #세로 check
    for j in range(3):
        ones,twos=0,0
        for i in range(3):
            current=ttt[i][j]
            if current==1: ones+=1
            elif current==2: twos+=1
        if ones==3: print(1); exit(0)
        elif twos==3: print(2); exit(0)
    #대각선 check (\ 방향)
    if ttt[0][0]==1 and ttt[1][1]==1 and ttt[2][2]==1: print(1); exit(0)
    elif ttt[0][0]==2 and ttt[1][1]==2 and ttt[2][2]==2: print(2); exit(0)
    #대각선 check (/ 방향)
    if ttt[2][0]==1 and ttt[1][1]==1 and ttt[0][2]==1: print(1); exit(0)
    elif ttt[2][0]==2 and ttt[1][1]==2 and ttt[0][2]==2: print(2); exit(0)
print(0)
