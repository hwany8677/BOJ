#Filthy code
# from time import process_time as pt
def dashin(w,h,x,y,t):
    mode=1
    #mode 설명
    #1: x증가 y증가
    #2: x감소 y증가
    #3: x감소 y감소
    #4: x증가 y감소
    dash=1
    i=0
    while(t>0):
        #모서리 체크는 x에서 다 했기 때문에 y에서 두 번 반복할 필요 없음
        # print()
        # print(f"{i+1} 번째 반복")
        # print(f"현 좌표: {x} {y}")
        if (x==w):
            if (y==h): mode=3
            elif (y==0): mode=2
            else: mode=2 if mode==1 else 3
        elif (x==0):
            if (y==0): mode=1
            elif (y==h): mode=4
            else: mode=4 if mode==3 else 1
        if (y==h): mode=4 if mode==1 else 3
        elif (y==0): mode=1 if mode==4 else 2
        calc=op(mode) #0: 더하기 1: 빼기
        if dash>t: dash=1

        if x+dash>w: dash=1
        if x-dash<0: dash=1
        if y+dash>h: dash=1
        if y-dash<0: dash=1

        if calc[0]==0: x+=dash
        elif calc[0]==1: x-=dash
        if calc[1]==0: y+=dash
        elif calc[1]==1:y-=dash
        # print(f"연산모드: {mode}번")
        # print(f"간 거리={dash}")
        # print(f"도착한 좌표: {x} {y}")
        t-=dash
        dash+=dash
        i+=1
    return f"{x} {y}"
def op(mode):
    if mode==1: return [0,0]
    if mode==2: return [1,0]
    if mode==3: return [1,1]
    if mode==4: return [0,1]  
w,h=map(int,input().split())
p,q=map(int,input().split())
t=int(input())
# t1=pt()
print(dashin(w,h,p,q,t))
# t2=pt()
# print(f"Time took to run: {t2-t1} seconds")