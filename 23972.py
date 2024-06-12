K,N=map(int,input().split())
extra,streak=1,1
while(extra+K<extra*N): 
  if (extra+streak>K): streak=1
  extra+=streak
  print("반복")
print(extra,streak)
print(extra+K)