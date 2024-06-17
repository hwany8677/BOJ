current=0
mx=0
for _ in range(10):
  off,aboard=map(int,input().split())
  delta=aboard-off
  current=current+delta
  mx=current if current>=mx else mx
print(mx)