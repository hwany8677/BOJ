#첫 위치: 1
m=int(input())
cup=[1,2,3]
for i in range(0,m):
    frm,to=map(int,input().split())
    cup[frm-1],cup[to-1]=cup[to-1],cup[frm-1]
    print(cup)
print(cup[0])