def dice(n,max):
	if n[0]==n[1] and n[1]==n[2]: return 10000+n[1]*1000
	if n[0]==n[1] or n[1]==n[2]: return 1000+n[1]*100
	if n[0]==n[2]: return 1000+n[0]*100
	return max*100
n=input().split()
max=0
for i in range(0,3): 
	n[i]=int(n[i])
	if max<n[i]: max=n[i]
print(dice(n,max))
