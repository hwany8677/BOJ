input=open(0).readline
m,n,k=map(int,input().split())
buf=[]
for _ in range(m): buf.append(input().rstrip())
for row in buf:
    for _ in range(k):
        for col in row: print(col*k,end='')
        print()
