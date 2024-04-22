#Might take too long...or is it?
#from math import sqrt
m=int(input())
n=int(input())
if m>n: m,n=n,m #To make m<n
sum=0
min=0
i=1
while(True):
	temp=i**2
#	print(f"temp: {temp}")
	if temp>=m and temp<=n: 
		sum+=temp
		if min==0: min=temp
	if temp>n: break
	i+=1
if sum>0: 
	print(sum)
	print(min)
else: print(-1)
