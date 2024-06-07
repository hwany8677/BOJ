#이게 뭐라고...ㅠ...5시간을...
#시간은...새벽 2시반...
# from time import process_time as p
# def gridPrint(grid):
#     for i in range(len(grid)): print(grid[i])
def seek(grid,C,R): #R,C=5,6
    x,y,pos=0,0,1
    op,dir=5,0
    i=1
    # op 설명
    # 1,2는 +이고 3,4는 -임. 반복문 끝에서 +=1 시전.
    # 만약 다음 반복에서 5가 될 경우 1로 리셋.
    #
    # dir 설명
    # 0은 y고 x는 1임. 반복문 끝에서 0이면 1로, 1이면 0으로 변경.
    realC=len(grid)
    realR=len(grid[0])
    while (pos!=k):
        if op==5: op=1
        # print()
        # gridPrint(grid)
        # print(f"현재 반복 {i}번째")
        # print(f"방향: {"y (0)" if dir==0 else "x (1)"}")
        # print(f"연산자: {"+" if op==1 or op==2 else "-"} ({op})")
        # print(f"좌표: ({x+1},{y+1})")
        # print(f"자리: {pos}번")
        #벽 검사
        if (pos>=realR+realC+realR-3): #첫 줄은 예외
            if dir==0: #y
                if (grid[x][y+(R if op<=2 else -R)]): 
                    R-=1
            elif dir==1: #x
                if (grid[x+(C if op<=2 else -C)][y]): 
                    C-=1
        # print(f"C={C}, R={R}")
        pos+=R if dir==0 else C #위치 변경
        #좌표 변경 및 처음과 (처음+1), 끝과 (끝-1)을 1로 지정
        if dir==0: 
            grid[x][y]=1
            temp=y+1 if op<=2 else y-1 #처음
            grid[x][temp]=1
            y=y+R if op<=2 else y-R #좌표변경
            grid[x][y]=1
            temp=y-1 if op<=2 else y+1 #끝
            grid[x][temp]=1
        elif dir==1: 
            grid[x][y]=1
            temp=x+1 if op<=2 else x-1 #처음
            grid[temp][y]=1
            x=x+C if op<=2 else x-C #좌표변경
            grid[x][y]=1
            temp=x-1 if op<=2 else x+1 #끝
            grid[temp][y]=1
        #pos와 찾고자하는 k 확인
        if pos>=k: 
            # print()
            # gridPrint(grid)
            # print("자리를 찾았다!")
            if op<=2:
                return f"{x+1-(pos-k)} {y+1}" if dir==1 else f"{x+1} {y+1-(pos-k)}"
            else:
                return f"{x+1+(pos-k)} {y+1}" if dir==1 else f"{x+1} {y+1+(pos-k)}"
        op+=1
        dir=1 if dir==0 else 0
        i+=1
    return "1 1" if x==y==0 else f"{x} {y}"
C,R=map(int,input().split())
k=int(input())
grid=[]
# t0=p()
for _ in range(C): grid.append([0 for _ in range(R)])
if k>C*R: print(0)
else: print(seek(grid,C-1,R-1))
# t=p()
# print(grid[0])
# print(f"Time took to process: {t-t0} seconds")