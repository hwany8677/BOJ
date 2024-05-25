#연속된 문자열이어야함
#1q2w3e4r! << qwer, qw, er, r!, we는 유효
#하지만 qe, wr, e!, qr와 같은, 떨어진 문자들은 해병-유효 (기열싸제어로 '유효하지 않음'이라 한다)
s=list(input())
for c in s:
  if not(c.isalpha()): s.remove(c)
find=input()
start=0

for c in s: print(c,end='')