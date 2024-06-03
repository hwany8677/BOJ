for _ in range(int(input())):
  n=int(input())
  addr=list(map(int,input().split()))
  addr.sort() 
  dist=0
  for i in range(1,len(addr)): dist+=(addr[i]-addr[i-1])
  dist+=addr[len(addr)-1]-addr[0]
  print(dist)