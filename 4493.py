#다중if문 again
#아니잠만ㅅㅂ1928ms?????
#이때는 PyPy가 진리다...
t=int(input())
for _ in range(0,t): 
  n=int(input())
  p1,p2=0,0
  for i in range(0,n): 
    s=input() 
    if s[0]==s[2]: continue
    if s=="P R" or s=="R S" or s=="S P": p1+=1
    else: p2+=1
  print("Player 1" if p1>p2 else "Player 2" if p1<p2 else "TIE")