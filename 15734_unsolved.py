# 1 5 2
# l과 r중 적은 쪽에 2를 더함
# 3 5 0
# l=r 될때까지 l과 r중 큰걸 뺌
# 3 3 0 -> l+r=6
# 7 7 7
# l과 r이 이미 같으므로 a를 기준으로 생각함
# 8 8 5
# 9 9 3
# 10 10 1
# a<2이므로 중단 -> l+r=10
l,r,a=map(int,input().split())
if l==r:
  while (a>2):
    l+=1
    r+=1
    a-=2
elif l<r:
  while (l!=r):
    if a<1: break
    l+=1
    a-=1
  if l<r:
    while(l!=r): r-=1
elif l>r:
  while (l!=r):
    if a<1: break
    r+=1
    a-=1
  if l>r:
    while(l!=r): l-=1
print(l+r)