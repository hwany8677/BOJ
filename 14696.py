#별 > 동그라미 > 네모 > 세모 순으로 비교.
#사실 2456번이랑 흐름은 비슷함
#무승부: D
#★: 4, ●: 3, ■: 2, ▲: 1
n=int(input())
for _ in range(n):
  buf=list(map(int,input().split()))
  buf=tuple(buf[1:]) 
  a=[]
  #Does saving converted data to somewhere else makes the program any faster?
  #I wonder...
  # for num in range(4,0,-1): a.append(tuple(buf).count(num))
  for num in range(4,0,-1): a.append(buf.count(num))
  buf=list(map(int,input().split()))
  buf=tuple(buf[1:])
  b=[]
  for num in range(4,0,-1): b.append(buf.count(num))
  if a[0]>b[0]: print("A")
  elif a[0]<b[0]: print("B")
  else:
    if a[1]>b[1]: print("A")
    elif a[1]<b[1]: print("B")
    else:
      if a[2]>b[2]: print("A")
      elif a[2]<b[2]: print("B")
      else:
        if a[3]>b[3]: print("A")
        elif a[3]<b[3]: print("B")
        else: print("D")