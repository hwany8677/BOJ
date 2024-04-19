while(True):
	n=int(input())
	if n==-1: break
	sum=1
	div=[]
	for i in range(2,n): 
		if (n%i==0): 
			sum+=i
			div.append(i)
	if (sum==n):
		print(f"{n} = 1 +",end='')
		for i in range(0,len(div)-1): 
			print(f" {div[i]}",end=' +')
		print(f" {div[len(div)-1]}")
	else: print(f"{n} is NOT perfect.")