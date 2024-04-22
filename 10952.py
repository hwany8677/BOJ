res=[]
while(True):
	a,b=map(int,input().split())
	if (a==0 and b==0): break
	res.append(a+b)
for i in res: print(i)
