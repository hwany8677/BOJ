#생각보다 긴데?
#"{:.3f}".format()
#기준: a²+b²=c²
from math import sqrt
a,b,c=map(int,input().split())
n=1
while(a!=0 or b!=0 or c!=0):
  print(f"Triangle #{n}")
  if (a==0 or b==0 or c==0): print("Impossible.",end='')
  elif a==-1:
    a=c**2-b**2
    print("a = "+"{:.3f}".format(sqrt(a)) if a>0 else "Impossible.")
  elif b==-1:
    b=c**2-a**2
    print("b = "+"{:.3f}".format(sqrt(b)) if b>0 else "Impossible.")
  elif c==-1:
    c=a**2+b**2
    print("c = "+"{:.3f}".format(sqrt(c)) if c>0 else "Impossible.")
  n+=1
  print()
  a,b,c=map(int,input().split())