#'mod' = 우리가 흔히 말하는 '나머지'
l=int(input())
s=input()
hash=0
r,M=31,1234567891
for i in range(0,l): 
  hash+=( (ord(s[i])-96)*(r**i) )
print(hash%M)