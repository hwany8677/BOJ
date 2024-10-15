#1 - 밑으로
#2 - 위로
#3 - 선택 후 밑으로
#4 - 선택 후 위로
#커서는 맨 위부터 시작
input=open(0).readline
pos_kb1,pos_kb2=0,0
for i in range(int(input())): 
    buf=input().rstrip()
    if buf=='KBS1': pos_kb1=i
    if buf=='KBS2': pos_kb2=i
#특수한 경우 제외하고 모든 방법이 출력이 될 수 있음
if pos_kb1==1 and pos_kb2==2: print("33")
elif pos_kb1==1 and pos_kb2==2: print("3")
elif pos_kb1>pos_kb2: print("1"*pos_kb1,"4"*pos_kb1,"1"*(pos_kb2+1),"4"*pos_kb2,sep='')
else: print("1"*pos_kb2,"4"*pos_kb2,"1"*(pos_kb1+1),"4"*pos_kb2,sep='')



























#정성을 다~하~는~
#국 민 의 방 송~
#K B S~~~~~
#한국 방 송~
