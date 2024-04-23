n=int(input())
s=[]
for i in range(0,n*2):
    if (i+1)%2!=0: s.append("*")
    else: s.append(" ")
for i in range(0,n):
    for j in s: print(j,end='')
    s.reverse()
    print()