#얼 탱
xs,ys=map(int,input().split()) #승강장
xe,ye,dx,dy=map(int,input().split()) #기차
if dx==0: print(xe,ys)
elif dy==0: print(xs,ye)
else:
    if dx>0:
        t=dy/dx
        mn=2147483647
        res_x,res_y=0,0
        for x in range(xe,101):
            y=t*(x-xe)+ye
            str_y=str(y).split('.')
            dist=((x-xs)**2+(y-ys)**2)
            # print(f"x={x},y={y}")
            # print(f"dist={dist}")
            if dist<mn and str_y[1]=='0':
                mn=dist
                res_x=x
                res_y=int(y)
        print(res_x,res_y)
    elif dx<0:
        t=dy/dx
        mn=2147483647
        res_x,res_y=0,0
        for x in range(xe,-101,-1):
            y=t*(x-xe)+ye
            str_y=str(y).split('.')
            dist=((x-xs)**2+(y-ys)**2)
            # print(f"x={x},y={y}")
            # print(f"dist={dist}")
            if dist<mn and str_y[1]=='0':
                mn=dist
                res_x=x
                res_y=int(y)
        print(res_x,res_y)
