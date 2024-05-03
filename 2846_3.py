#장난기 발동
n=int(input())
p=list(map(int,input().split()))
pv=0
m=0
for i in range(0,len(p)):
	if i+1==len(p) or p[i]>=p[i+1]:
		if p[i]-p[pv]>=m:
			m=p[i]-p[pv]
		pv=i+1
print(m)
