n=int(input())
while (True): 
  i=int(input())
  if not(i): break
  print(f"{i} is a multiple of {n}." if i%n==0 else f"{i} is NOT a multiple of {n}.")