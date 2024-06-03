#나~느으으은~ 행복합니다아아아~
#나~느으으은~! 행복합니다아아아~
#나~느으으은~ 행복합니다아아아~
#한화라서 행복합니 당당당당당당!!

#환화의 김성근 감독님 사랑해
#예 예 예 예예예 예 예 예 예예예 예 예 예 예예예 예 예 예 예예예 예 예 예 예예예 예 예 예 예예예 예 예 예 예예예 예 예 예 예예예
#환~화에ㅔㅔ~ 김~서엉근~ 감동님 사아아랑해애~
ulim=list(map(int,input().split()))
startlink=list(map(int,input().split()))
sigU,sigS=0,0
for i in range(0,8): 
  sigU+=ulim[i]
  sigS+=startlink[i]
areWeWinning=sigU>sigS #코드 수정 필요: 1회차때 이기고 2~8회차때 점수변동 없는 상황이 나올 수 있음
sigU+=ulim[8]
sigS+=startlink[8]
if areWeWinning and sigU<sigS: print("Yes")
else: print("No")