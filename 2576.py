min=101
s=0
for i in range(0,7):
	n=int(input())
	if n%2: 
		s+=n
		if min>n: min=n
if min==101: print(-1)
else:
	print(s)
	print(min)
