# BW 또는 WB에 대해 얼마나 많이 수정해야되는지 비교를함
#n->세로, m->가로
import copy #INTRODUCING - 'copy' MOUDLE!
def flip(n,m,board): 
    res=copy.deepcopy(board) #Helps copying n-dimensional lists 
    for i in range(n):
        for j in range(m):
            if res[i][j]=='B':
                res[i][j]='W'
            elif res[i][j]=='W':
                res[i][j]='B'
    return res
def countAll(inpuT, comp,n,m):
    count=0
    min_count=32767
    #n-8, m-8 기준으로 함
    for k in range(0,n-7):
        count=0
        for i in range(0+k,8+k):
            for l in range(0,m-7):
                count=0
                for j in range(0+l,8+l):
                    count+=1 if inpuT[i][j]!=comp[i][j] else 0
                if count<=min_count: min_count=count
        if count<=min_count: min_count=count
    return count
n,m=map(int,input().split())
board1=[]
board2=[]
#홀: W, 짝: B
#홀: WB, 짝: BW
for i in range(n):
    board1.append([])
    for j in range(m):
        if i%2==1: board1[i].append('W' if j%2==1 else 'B')
        else: board1[i].append('B' if j%2==1 else 'W')
board2=flip(n,m,board1)
input_board=[]
for i in range(n): input_board.append(input())
board1_count=countAll(input_board,board1,n,m)
board2_count=countAll(input_board,board2,n,m)
print(board1_count,board2_count)
# print(board1_count if board1_count<board2_count else board2_count)