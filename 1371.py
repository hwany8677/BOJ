#이게 왜 안풀려있지?
#아! A+B 4번 문제와 같은거구나!
import sys
s=[]
while(1):
  buf=sys.stdin.readline()
  if buf=='': break #EOF는 '상태' 이지 '문자'가 아니다!
  s.append(buf.split())
#print(*s)
alphabet=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,len(s)):
  for j in range(0,len(s[i])): 
    for k in range(0,len(s[i][j])):
      alphabet[ord(s[i][j][k])-97]+=1
#print(alphabet)
print(len(alphabet))
m=max(alphabet)
for i in range(0,26):
  if alphabet[i]==m: print(chr(i+97),end='')