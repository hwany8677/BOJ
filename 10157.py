# from time import process_time as p
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
    while (pos!=k):
        print(f"현재 반복 {i}번째")
        if op==5: op=1
        #벽 검사
        if (y==0 and x>0): #첫 줄은 예외
            if dir==0: #y
                if (grid[x][y+R]): R-=1
            elif dir==1: #x
                if (grid[x+C][y]): C-=1
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
            print(f"{x} {y}")
            grid[x][y]=1
            temp=x-1 if op<=2 else x+1 #끝
            grid[temp][y]=1
        #pos와 찾고자하는 k 확인
        if pos>=k: return f"{x+1-(pos-k)} {y+1}" if dir==1 else f"{x+1} {y+1-(pos-k)}"
        op+=1
        dir=1 if dir==0 else 0
        i+=1
    return f"{x} {y}"
C,R=map(int,input().split())
k=int(input())
grid=[]
# t0=p()
for _ in range(R): grid.append([0 for _ in range(C)])
R-=1
C-=1
print(seek(grid,C,R))
# t=p()
# print(grid[0])
# print(f"Time took to process: {t-t0} seconds")