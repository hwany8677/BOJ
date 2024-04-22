#Filthy code
personName=[] #Self-explanatory
bdate=[] #Stored in total days
leap=[1992, 1996, 2000, 2004, 2008]
month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
n=int(input())
max,min=0,0
for i in range(0,n):
	t=0 #Jan 1 1990 as Day 1, Dec 31st 2010 as Day 7670
	buf=input().split()
	personName.append(buf[0])
	yr=int(buf[3])
	m=int(buf[2])
	d=int(buf[1])
	isLeap=False
	howManyL=0
	#Normal year: 365 days, leap year: 366 days
	for j in leap:
		#Skips two if statements when yr=1992
		if yr<j: break #Exclude 1990, 1991
		if j<yr: howManyL+=1 #To exclude the same year(=yr) getting added
		if j==yr: isLeap=True
	t+=(yr-1990)*365+howManyL
#	print(f"Year added, t={t}")
	#Month
	for k in range(1,m): t+=month[k]
	if isLeap:
		if (m==2 and d==29) or m>=3: 
			t+=1
#	print(f"Month added, t={t}")
	#Day
	t+=d
#	print(f"Day added, t={t}")
	bdate.append(t)
	#Yongest & Oldest
	if bdate[i]>=bdate[max]: max=i
	if bdate[i]<=bdate[min]: min=i
#print(f"nameDB: {personName}")
#print(f"bdate: {bdate}")
print(personName[max])
print(personName[min])
