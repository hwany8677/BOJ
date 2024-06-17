#for문 안에서 str 변환을 쓰면 느려진다!? 뿌슝빠슝삐슝!????
n=int(input())
count=0
for i in range(n+1):
  for c in str(i): 
    if c=='3' or c=='6' or c=='9': count+=1
print(count)