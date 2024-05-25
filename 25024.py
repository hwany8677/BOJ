#Just a warm-up
t=int(input())
for _ in range(0,t):
  x,y=map(int,input().split())
  if (x<24 and y<60): print("Yes ",end='')
  else: print("No ",end='')
  if (x==0 or y==0):
    print("No")
    continue
  if (y==31): #31일이면 작동됨
    if (x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12): 
      print("Yes")
      continue
    else: 
      print("No")
      continue
  if (x==2): #and문으로 작성시 짜기가 곤란해짐
    if (y<30): 
      print("Yes")
      continue
    else: 
      print("No") 
      continue
  if (x<13 and y<32): print("Yes")
  else: print("No")