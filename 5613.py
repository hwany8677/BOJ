res=int(input())
while (1): 
  op=input()
  if op=='=': break 
  n=int(input())
  if op=='+': res+=n
  if op=='-': res-=n
  if op=='*': res*=n
  if op=='/': res=int(res/n)
print(res)