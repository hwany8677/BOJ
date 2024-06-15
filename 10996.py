#Memory
n=int(input())
for i in range(2*n):
  buf=[]
  for j in range(1,n+1): 
    if j%2: buf.append("*" if not(i%2) else " ")
    elif not(j%2): buf.append(" " if not(i%2) else "*")
  print(*buf,sep='')