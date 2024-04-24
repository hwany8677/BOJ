#Straightforward
n,k=map(int,input().split())
yaksu=[]
for i in range(1,n+1):
	if not(n%i): yaksu.append(i)
if len(yaksu)<k: print(0)
else: print(yaksu[k-1]) #이미 순서대로 정렬되어 있음
