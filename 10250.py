#배열을 미리 생성하는 풀이
t=int(input())
for _ in range(0,t):
  roomNo=[0]
  h,w,n=map(int,input().split())
  for i in range(1,w+1): 
    for j in range(1,h+1):
      roomNo.append(str(j)+str(i).zfill(2))
  print(roomNo[n])