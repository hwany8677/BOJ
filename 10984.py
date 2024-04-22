#GPA = Total Grade Points(=Credit*Score) / Total Credit
t=int(input())
for i in range(0,t):
	cr,gr=0,0
	n=int(input())
	for j in range(0,n):
		c,g=input().split()
		cr+=int(c)
		gr+=int(c)*float(g)
	print(cr,"{:.1f}".format(gr/cr))