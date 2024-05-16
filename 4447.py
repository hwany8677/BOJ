n = int(input())
for _ in range(0, n):
  s = input()
  gc, bc = 0, 0
  for i in range(0, len(s)):
    if s[i] == 'g' or s[i] == 'G': gc += 1
    if s[i] == 'b' or s[i] == 'B': bc += 1
  print(f"{s} is GOOD" if gc > bc else f"{s} is NEUTRAL" if gc == bc else f"{s} is A BADDY")
