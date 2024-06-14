from sys import stdin
buf=[]
for _ in range(10): buf.append(int(stdin.readline()))
avg=int(sum(buf)/10)
entry=dict()
for i in range(10):
  if (buf[i] not in entry): entry[buf[i]]=1
  else: entry[buf[i]]+=1
print(avg)
print(max(entry,key=entry.get))