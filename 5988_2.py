#Method 2
for _ in range(int(input())):
  n=int(input())
  n=list(str(n))
  print("even" if int(n[len(n)-1])%2==0 else "odd")