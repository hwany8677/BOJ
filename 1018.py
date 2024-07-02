# BW 또는 WB에 대해 얼마나 많이 수정해야되는지 비교를함
#n->세로, m->가로
def flip(n,m,board):
    for i in range(n):
        for j in range(m):
            board[i][j]='W' if board[i][j]=='B' else 'B'
            board[i][j]='B' if board[i][j]=='W' else 'W'
    return board
n,m=map(int,input().split())
board=[]
board2=[]
#홀: W, 짝: B
#홀: WB, 짝: BW
for i in range(n):
    board.append([])
    for j in range(m):
        if i%2==1: board[i].append('W' if j%2==1 else 'B')
        else: board[i].append('B' if j%2==1 else 'W')
board2=flip(n,m,board)

input_board=[]
for i in range()
