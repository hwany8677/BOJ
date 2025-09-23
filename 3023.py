input=open(0).readline
r,c=map(int,input().split())
quarter=[]
for _ in range(r):
    quarter.append(input().rstrip())
a,b=map(int,input().split())
res=[]
for i in range(r): res.append(list(quarter[i])+list(quarter[i][::-1]))
for i in range(r-1,-1,-1): res.append(list(quarter[i])+list(quarter[i][::-1]))
if res[a-1][b-1]=='.': res[a-1][b-1]='#'
else: res[a-1][b-1]='.'
for i in range(2*r):
    for j in range(2*c): print(res[i][j],end='')
    print()