n=int(input())
s=input()
buf=[[]]
direction=False
row=0
for i in range(len(s)):
    #i%n==n-1마다 방향 바꾸기
    buf[row].append(s[i])
    if i%n==n-1: 
        if direction: buf[row].reverse()
        direction=not(direction)
        buf.append([])
        row+=1
if len(buf[row])==0: buf.pop(len(buf)-1)
for i in range(n):
    for j in range(len(buf)): print(buf[j][i],end='')
print()
