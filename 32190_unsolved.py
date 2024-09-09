n=int(input())
buf=[]
for i in range(2,n+1): 
    if not(i%2): buf.append(i)
buf.append(1)
for i in range(n,0,-1): 
    if not(i%2): buf.append(i)
for i in range(3,n+1): 
    if i%2: buf.append(i)
buf.append(1)
for i in range(n,1,-1):
    if i%2: buf.append(i)
print(*buf)