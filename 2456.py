#얻은 교훈
#다 같아보여도 세부적으론 다른 경우가 있다.
#23행~33행을 못적어서 시간을 날렸다~
one,two,three=[0,[],[],[]],[0,[],[],[]],[0,[],[],[]]
for _ in range(int(input())):
    ga,na,da=map(int,input().split())
    one[ga].append(ga)
    two[na].append(na)
    three[da].append(da)
sum1=sum(one[1])+sum(one[2])+sum(one[3]) #1번 후보의 합계
sum2=sum(two[1])+sum(two[2])+sum(two[3]) #2번 후보의 합계
sum3=sum(three[1])+sum(three[2])+sum(three[3]) #3번 후보의 합계
biggest=max(sum1,sum2,sum3) #그중 큰것
if (sum1>sum2 and sum1>sum3): print(1, biggest)
elif (sum2>sum3 and sum2>sum1): print(2, biggest)
elif (sum3>sum1 and sum3>sum2): print(3, biggest)
else: #세부비교 시작
    bigs=[]
    if sum1==biggest: bigs.append(1)
    if sum2==biggest: bigs.append(2)
    if sum3==biggest: bigs.append(3)
    #3점 및 2점 세부비교
    if bigs==[1,2,3]:
        if one[3]==two[3]==three[3]:
            if one[2]==two[2]==three[2]: print(0,biggest)
            else: 
                if one[2]>two[2] and one[2]>three[2]: print(1, biggest)
                elif two[2]>one[2] and two[2]>three[2]: print(2, biggest)
                elif three[2]>one[2] and three[2]>two[2]: print(3, biggest)
        else:
            if one[3]>two[3] and one[3]>three[3]: print(1, biggest)
            elif two[3]>one[3] and two[3]>three[3]: print(2, biggest)
            elif three[3]>one[3] and three[3]>two[3]: print(3, biggest)
    if bigs==[1,2]:
        if one[3]==two[3]:
            if one[2]==two[2]: print(0, biggest)
            else: print(1 if one[3]>two[3] else 2,biggest)
        else: print(1 if one[3]>two[3] else 2,biggest)
    if bigs==[1,3]:
        if one[3]==three[3]:
            if one[2]==three[2]: print(0, biggest)
            else: print(1 if one[2]>three[3] else 3,biggest)
        else: print(1 if one[3]>three[3] else 3,biggest)
    if bigs==[2,3]:
        if two[3]==three[3]:
            if two[2]==three[2]: print(0, biggest)
            else: print(2 if two[2]>three[3] else 3,biggest)
        else: print(2 if two[3]>three[3] else 3,biggest)