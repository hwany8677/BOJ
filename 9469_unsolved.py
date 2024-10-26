#상대속도로 등비급수하는 문제
#솔직히 태그에 왜 사칙연산 들어가있는지 모르겠음 (등비급수, 물리학 필요)
input=open(0).readline
for i in range(1,1+int(input())):
    buf=input().split()
    d=float(buf[1])
    a=float(buf[2])
    b=float(buf[3])
    f=float(buf[4])
    res=0.0
    while(1):
        #A의 관성계에서 바라본 F -> B 계산
        A_fake_b=b-a
        A_fake_f=f-a
        B_fake_f=f-b
        B_fake_b=0
        t_collide_FtoB=d/B_fake_f
        d+=b*t_collide_FtoB
        
        #A의 관성계에서 바라본 F -> A 계산
        A_fake_f=a+f
        t_collide_FtoA=d/A_fake_f
        delta=b*t_collide_FtoA
