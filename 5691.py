#a, b, c의 평균값=a, b, c의 중앙값 (그것도 "최소")
while(1):
  a,b=map(int,input().split())
  if (a==b==0): break
  c=2*b-a
  minC=c
  avg=int((a+b+c)/3) #a, b, c는 정수임
  minC=c if c<=minC and b==avg else minC
  c=int((a+b)/2)
  avg=int((a+b+c)/3)
  minC=c if c<=minC and c==avg else minC
  c=2*a-b
  avg=int((a+b+c)/3)
  minC=c if c<=minC and a==avg else minC
  print(minC)