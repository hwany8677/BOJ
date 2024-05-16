t=int(input())
for _ in range(0,t): 
  s=list(input())
  if ord(s[0])>=97: s[0]=chr(ord(s[0])-32)
  for c in s: print(c,end='')
  print()