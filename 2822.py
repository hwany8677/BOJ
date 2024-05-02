#Filthy code
#문제에서 원하는것: 레이팅 시스템을 만들어라
sc=[]
num=[1,2,3,4,5,6,7,8]
for i in range(0,8): sc.append(int(input()))
for i in range(0,8):
	for j in range(1,8):
		if sc[j-1]>sc[j]:
			sc[j-1],sc[j]=sc[j],sc[j-1]
			num[j-1],num[j]=num[j],num[j-1]
s=0
for i in range(3,8): 
	for j in range(4,8):
		if num[j-1]>num[j]: num[j-1],num[j]=num[j],num[j-1]
	s+=sc[i]
print(s)
for i in range(3,8): print(f"{num[i]} ",end='')
print()
