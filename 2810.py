#S -> at least one people
#L -> at least two people
#When there's LL and LL seats consequently, total cup -=1
#S and S -> don't do anything
#S and LL -> unless it's first seat, total cup-=1
#LL and S -> unless it's last seat, total cup-=1
#LL and LL -> total cup-=1
#...를 계획했으나 21%에서 계속 WA가 떠서 포기
#최종 소요시간 50분
n=int(input())
buf=input()
s,ll=0,0
i=0
while(i<len(buf)):
    if buf[i]=='S': s+=1; i+=1
    elif buf[i]=='L': ll+=1; i+=2
if ll==0: print(s)
else: print(n+1-ll)

