#갑을 병정 무기 경신 임계 - 십간 (0~9)
#자축 인묘 진사 오미 신유 술해 - 십이지 (A~L)
#10과 12의 LCM: 60
#2013년: F9, 전체 반복의 30번째 해에 있음
#그러므로 1984년에 A0임 (1번째)
#1924년, 1954년, 1984년, 2044년, 2074년, ...
#1년: J7, 2년: K8, 3년: L9
#4년: A0, 64년: A0
shipGan=[str(i) for i in range(10)]
shipiji=[c for c in "ABCDEFGHIJKL"]
res=[]
i,j=0,0
while "L9" not in res:
  res.append(shipiji[j]+shipGan[i])
  i=0 if i==9 else i+1
  j=0 if j==11 else j+1
#60으로 나눈 나머지로 처리.
yr=int(input())
print(res[(yr%60)-4])