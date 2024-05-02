#Why use 2D when you can do 2 for loops?
max=-1
a,b=0,0
for i in range(0,9):
	buf=input().split()
	for j in range(0,9):
		if int(buf[j])>=max:
			max=int(buf[j])
			a,b=i,j
print(max)
print(a+1,b+1)	
#But it used more memory??? tf?
