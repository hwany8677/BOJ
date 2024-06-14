from sys import stdin
s=[]
for _ in range(3): s.append(stdin.readline())
compare='0'
streak=1
mx=0
for i in range(3):
  for j in range(len(s[i])): 
    if s[i][j]==compare: streak+=1
    else:
      compare=s[i][j]
      mx=streak if streak>=mx else mx
      streak=1
  print(mx)
  mx=0