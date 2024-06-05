#조금더 짧게
#isalpha + 양쪽이비는건 'h'으로 고정
n=int(input())
s=list(input())
for i in range(n):
  if s[i].isalpha(): s[n-1-i]=s[i]
for i in range(n):
  if s[i]=='?': s[i]='h'
print(*(s),sep='')