#uh...I calculate e???
from math import factorial
print("n e")
print("- -----------")
n=10
for cr_n in range(0,n): 
  print(cr_n,end='') 
  print(" ",end='')
  e=0
  for i in range(0,cr_n+1): e+=1/factorial(i)
  print("{:.9f}".format(e) if cr_n>2 else "2.5" if cr_n==2 else int(e))