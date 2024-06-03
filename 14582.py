#항상 sigU<sigS 엔딩임. 고로 이겼는지 안 이겼는지만 보면됨.
#이걸 깨닫느라 시간 다씀 (댕청)
ulim=list(map(int,input().split()))
startlink=list(map(int,input().split()))
sigU,sigS=0,0
state=''
wasWinning=False #W -> L 전환 확인용
for i in range(0,9): 
  for _ in range(ulim[i]):
    sigU+=1
    if sigU>sigS: wasWinning=True 
  for _ in range(startlink[i]):
    sigS+=1
    if sigU>sigS: wasWinning=True
if wasWinning: print("Yes")
else: print("No")

#나~느으으은~ 행복합니다아아아~
#나~느으으은~! 행복합니다아아아~
#나~느으으은~ 행복합니다아아아~
#한화라서 행복합니 당당당당당당!!

#환화의 김성근 감독님 사랑해
#예 예 예 예예예 예 예 예 예예예 예 예 예 예예예 예 예 예 예예예 예 예 예 예예예 예 예 예 예예예 예 예 예 예예예 예 예 예 예예예
#환~화에ㅔㅔ~ 김~서엉근~ 감동님 사아아랑해애~

#삐익↗ 삑 삑삑삑!
#최!📣강!📣한!📣화!📣
#삐익 삑 삑삑삑!
#최!📣광!📣홯!📣으하!📣