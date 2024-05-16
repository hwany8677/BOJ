#뜬금없는 EOF
import sys
while True:
  s=sys.stdin.readline()
  if s=='': break
  a,b=int(s[0]),int(s[2])
  print(a+b)