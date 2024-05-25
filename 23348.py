a,b,c=map(int,input().split())
n=int(input())
m=0
for _ in range(0,n):
  skills=[0,0,0]
  s=0
  for i in range(0,3):
    skills[i]=list(map(int,input().split())) #동아리원이 사용한 기술 개수
    s+=skills[i][0]*a
    s+=skills[i][1]*b
    s+=skills[i][2]*c
  if s>=m: m=s
print(m)