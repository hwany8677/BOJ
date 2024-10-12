#깡으로 곱해주는 문제로 착각 ㄴㄴ
precalc=[0,0,[6,2,4,8],[1,3,9,7],0,0,0,[1,7,9,3],[6,8,4,2]] #2, 3, 7, 8
input=open(0).readline
for _ in range(int(input())):
    a,b=map(int,input().split())
    a%=10
    if a==0: print(10)
    elif a==1: print(1)
    elif a==4: print(4 if b%2 else 6)
    elif a==5: print(5)
    elif a==6: print(6)
    elif a==9: print(9 if b%2 else 1)
    else: print(precalc[a][b%4])