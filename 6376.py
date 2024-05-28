#uh...I calculate e???
from math import factorial, ceil, floor
def n_round(n):
  if n - floor(n) < 0.5:
      return floor(n)
  return ceil(n)
print("n e")
print("- -----------")
n=9
for cr_n in range(0,n): 
  print(cr_n,end='') 
  print(" ",end='')
  e=0
  for i in range(0,cr_n+1): e+=1/factorial(i)
  print(e if type(e)==type(2.7) else int(e))
