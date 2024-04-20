#Copied from 1934.py

#Euclidean algorithm
#lcd(a,b)=ab/gcd(a,b)
#a=bq+r where q=a//b and r=a%b
def GCD(a,b):
	if a<b: a,b=b,a
	i=2 #Start dividing by 2
	r=-1
	gcd=a*b #If two numbers are mutually prime
	while(True):
		q=a//b
		r=a%b
#		print(f"{a}={b}*{q}+{r}")
		if r==0: 
			return gcd
		a,b=b,r
	gcd/=b #Since b=gcd(a,b)
	return gcd
#	print(f"b={b}")
def LCD(a,b):
	lcd=a*b/GCD(a,b) 
	return lcd
a,b=map(int,input().split())
print(f"{GCD(a,b)}\n{LCD(a,b)}")
