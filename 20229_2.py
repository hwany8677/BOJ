#문제 1: *를 for문으로 출력하니 O(n)의 지연시간을 더 만들게됨
#문제 2: stdin에서 바로 입력을 받질 않으니 지연시간이 더 늘어남 (ㅅㅂ 이거 안하니 지연시간 ㅈ됨)
from sys import stdin
n,k,l=map(int,input().split())
qualified=0
rating=[]
for i in range(0,n):
  x1,x2,x3=map(int,stdin.readline().split())
  if x1<l or x2<l or x3<l: continue
  sigma=x1+x2+x3
  if sigma>=k:
    qualified+=1
    for r in [x1,x2,x3]: rating.append(r)
print(qualified)
print(*rating)