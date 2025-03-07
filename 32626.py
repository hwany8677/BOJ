#답은 0, 1, 2중 하나
#P와 s와 e가 한 직선상에 있지만, s와 e 사이에 없음 -> 0
#s와 e가 한 직선상에 있지만, P가 그 직선 위에 없음 -> 0
#P가 s와 e가 만드는 '평면'상에 없음 -> 1
#P가 s와 e사이에 있지만, s와 e가 만드는 직사각형의 모서리에 없음 -> 1
#P와 s와 e가 한 직선상에 있고, s와 e사이에 P가 있음 -> 2
sx,sy=map(int,input().split())
ex,ey=map(int,input().split())
px,py=map(int,input().split())
if (sy==ey): 
    if ex<sx: sx,ex=ex,sx #s와 e가 순서가 바뀌면 비교가 이상하게됨
    print(0 if (py!=sy or px<sx or ex<px) else 2)
elif (sx==ex): 
    if ey<sy: sy,ey=ey,sy
    print(0 if (px!=sx or py<sy or ey<py) else 2)
else: print(1)