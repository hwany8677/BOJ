#2D array in Python
nxn=[]
for i in range(0,9):
	buf=input().split()
	for j in range(0,9): buf[j]=int(buf[j])
	nxn.append(buf)
a,b=0,0
max=-1
for i in range(0,9):
	for j in range(0,9):
		if nxn[i][j]>=max:
			max=nxn[i][j]
			a,b=i,j
print(max)
print(a+1,b+1)
