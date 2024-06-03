#Simple.
s=input()
while (s!="*"):
  alpha=[0 for i in range(26)]
  count=0
  for c in s: 
    if ord(c)==32: continue
    alpha[ord(c)-97]+=1
    if alpha[ord(c)-97]==1: count+=1
  print("Y" if count>=26 else "N")
  s=input()