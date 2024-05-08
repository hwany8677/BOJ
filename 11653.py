#Time complexity: O(sqrt(n)) (According to GPT)
#Therefore: takes 1 seconds if n>=100,000,000
def prime(n):
	if (n==1): return
	i=2
	while(n!=1):
		if (n%i==0):
			print(i)
			n=n//i
		else:
			i+=1
n=int(input())
prime(n)
