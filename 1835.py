#오른쪽 맨 뒤 -> 왼쪽 맨 앞
from collections import deque
n=int(input())
p=deque()
length=1
while(n>0):
    p.appendleft(n)
    count=n
    while(count>0):
        append=p.pop()
        p.appendleft(append)
        count-=1
    n-=1
print(*p)