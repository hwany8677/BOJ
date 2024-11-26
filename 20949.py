#배울점: 기준에 우선순위를 둘 수 있음
input=open(0).readline
n=int(input())
ppi=[]
for i in range(1,n+1):
    w,h=map(int,input().split())
    ppi.append((i,w**2+h**2))
ppi.sort(key=lambda x: (-x[1],x[0]))
prev=0
for element in ppi: print(element[0])