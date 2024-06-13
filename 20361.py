#Filthy code
#Slowass code (4160ms)
from sys import stdin
N,X,K=map(int,input().split())
for _ in range(K): 
  frm,to=map(int,stdin.readline().split())
  if frm==X: X=to
  elif to==X: X=frm
print(X)