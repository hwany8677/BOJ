#영=10￦/30sec, 민=15￦/60sec
#'구간'
n=int(input())
buf=input().split()
y,m=0,0
for i in range(0,n): 
    buf[i]=int(buf[i])
    y+=((buf[i]//30)+1)*10
    m+=((buf[i]//60)+1)*15
print(f"Y {y}" if y<m else f"M {m}" if y>m else f"Y M {y}",end='')