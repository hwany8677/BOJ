K,N=map(int,input().split())
extra,streak=0,1
if (N==1): print(-1)
else:
  while(extra+K>extra*N): 
    if (extra+streak>extra*K): streak=1
    extra+=streak
    streak+=1
    # print(streak,'',end='')
  # while(extra+K!=extra*N):
  #   extra-=1
    # print(extra,'',end='')
  print(extra+K)