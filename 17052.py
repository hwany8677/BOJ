#한 쪽 손상-> 반대편으로 매꾸기
#양 쪽 손상-> 겹치지 않는 글자로 매꾸기
from random import randint as r
n=int(input())
s=input()
alpha=[0 for _ in range(26)]
for i in range(n): 
  if s[i]!='?': alpha[ord(s[i])-97]=1
i,j=0,len(s)-1
s=list(s)
while(i<=j): 
  if s[i]=='?' and s[j]!='?': s[i]=s[j] 
  elif s[i]!='?' and s[j]=='?': s[j]=s[i] 
  elif s[i]==s[j]=='?': 
    a=r(1,26)
    b=False
    while(1):
      for k in range(26):
        if alpha[k]: a=r(1,26)
        else:
          b=True
          break 
      if b: break
    s[i]=chr(a+96)
    s[j]=chr(a+96)
  i+=1
  j-=1 
print(*(s),sep='')