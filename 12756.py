a_atk,a_life=map(int,input().split())
b_atk,b_life=map(int,input().split())
while(a_life>0 and b_life>0):
    a_life-=b_atk
    b_life-=a_atk
print('DRAW' if a_life<=0 and b_life<=0 else 'PLAYER A' if b_life<=0 else 'PLAYER B')