#Using built-in sets
#웃긴게 이게 더 김
n=int(input())
pM=[]
for _ in range(0,n):
  dice=list(map(int,input().split()))
  dice.sort()
  if len(set(dice))==1: pM.append(50000+dice[0]*5000)
  elif len(set(dice))==2 or len(set(dice))==3:
    if dice[0]==dice[1]==dice[2] or dice[1]==dice[2]==dice[3]:
      pM.append(10000+dice[1]*1000)
    elif dice[0]==dice[1]: 
      if dice[2]==dice[3]:
        pM.append(2000+dice[0]*500+dice[2]*500)
      else: pM.append(1000+dice[0]*100)
    elif dice[1]==dice[2] or dice[2]==dice[3]:
      pM.append(1000+dice[2]*100)
  elif len(set(dice))==4:
    pM.append(max(dice)*100)
print(max(pM))