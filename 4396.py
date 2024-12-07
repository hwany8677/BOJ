input=open(0).readline
n=int(input())
mine_info=[]
click_info=[]
for _ in range(n): mine_info.append(input().rstrip())
for _ in range(n): click_info.append(input().rstrip())
mines=[[0 for _ in range(n)] for _ in range(n)]
stepped=False
for i in range(n):
    for j in range(n):
        current=mine_info[i][j]
        if current=='*':
            if click_info[i][j]=='x': stepped=True
            if i>0: 
                if j>0: mines[i-1][j-1]+=1 #좌측 상
                mines[i-1][j]+=1 #상 
                if j<n-1: mines[i-1][j+1]+=1 #우측 상
            if j>0: mines[i][j-1]+=1 #좌측
            if j<n-1: mines[i][j+1]+=1 #우측
            if i<n-1:
                if j>0: mines[i+1][j-1]+=1 #좌측 하
                mines[i+1][j]+=1 #하
                if j<n-1: mines[i+1][j+1]+=1 #우측 하
for i in range(n):
    for j in range(n):
        click=click_info[i][j]
        mine=mine_info[i][j]
        if mine=='*' and stepped: print("*",end='')
        elif mine=='*' and not(stepped): print(".",end='')
        else:
            if click=='x': print(mines[i][j],end='')
            else: print(".",end='')
    print()