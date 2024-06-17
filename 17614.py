#간단하게 보자
#하지만 느려...
n=int(input())
count=0
for i in range(n+1): 
  s=str(i)
  for c in s: 
    if c=='3' or c=='6' or c=='9': count+=1
print(count)