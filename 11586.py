#심리상태: 1~3, the higher the angrier
s=[]
for _ in range(int(input())):
  s.append(input())
k=int(input())
if k==1: 
  for i in range(len(s)): print(s[i])
if k==2:
  for i in range(len(s)): 
    s[i]=list(s[i])
    s[i].reverse()
    for j in range(len(s[i])): print(s[i][j],end='')
    print()
if k==3:
  for i in range(len(s)-1,-1,-1): print(s[i])