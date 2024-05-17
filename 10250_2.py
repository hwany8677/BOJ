#반복문 only
#얼탱이 없는 오류 있어서 while문으로 대체
t=int(input())
for _ in range(0,t):
  h,w,n=map(int,input().split())
  c=1 
  i,j=1,1
#  for i in range(1,w+1): 
#    j=0
#    for j in range(1,h+1):
#      print(f"i: {i}, j: {j}")
#      print(str(j)+str(i).zfill(2))
#      if c==n: break
#      else: c+=1
  while(1):
    while(1):
      if c==n or j>h: break
      else: 
        c+=1
        j+=1
  print(str(j)+str(i).zfill(2))