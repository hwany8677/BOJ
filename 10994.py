#1 -> 5 -> 9 -> 13
#an=4n-3 (변의길이)
def starfill(n,buf,startpos): 
  if n>0: buf=starfill(n-1,buf,startpos+2)
  else: return buf
  start=startpos
  end=4*n-4+startpos
  for i in range(start,end+1): 
    buf[start][i]='*'
    buf[end][i]='*'
    buf[i][start]='*'
    buf[i][end]='*'
  return buf
n=int(input())
buf=[[' ' for _ in range(4*n-3)] for _ in range(4*n-3)]
buf=starfill(n,buf,0)
for i in range(4*n-3): print(*buf[i],sep='')