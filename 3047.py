#if문 지옥
n = list(map(int, input().split()))
n.sort()
order = input()
if order == "ABC":
  print(n[0], n[1], n[2])
if order == "BAC":
  print(n[1], n[0], n[2])
if order == "BCA":
  print(n[1], n[2], n[0])
if order == "CAB":
  print(n[2], n[0], n[1])
if order == "CBA":
  print(n[2], n[1], n[0])
