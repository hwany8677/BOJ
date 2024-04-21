#Euclidean algorithm
#LCD(a,b)=ab/gcd(a,b)
def LCD(a,b):
	if a<b: a,b=b,a
	r=-1
	lcd=a*b
	while(True):
		q=a//b
		r=a%b
#		print(f"{a}={b}*{q}+{r}")
		if r==0: break
		a,b=b,r
#	print(f"b={b}")
	lcd/=b #Since b=gcd(a,b)
	return int(lcd)
t=int(input())
for i in range(0,t):
	a,b=input().split()
	a=int(a)
	b=int(b)
	print(LCD(a,b))
