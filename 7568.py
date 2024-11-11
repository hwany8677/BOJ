#'확실하게 나보다 작으면' 다 세보기
n=int(input())
info=[]
for _ in range(n): 
    x,y=map(int,input().split())
    info.append((x,y))
pos=[0 for _ in range(n)]
for i in range(n):
    cur_x,cur_y=info[i][0],info[i][1]
    for j in range(n):
        if i==j: continue
        comp_x,comp_y=info[j][0],info[j][1]
        if cur_x<comp_x and cur_y<comp_y: pos[i]+=1
for i in range(n): print(pos[i]+1,end=' ')
print()
