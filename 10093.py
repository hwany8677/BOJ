a,b=map(int,input().split())
if a>b: a,b=b,a
temp=b-a-1
if temp<1: print(0); exit(0)
else: print(temp)
for i in range(a+1,b): print(f"{i} ",end='')
