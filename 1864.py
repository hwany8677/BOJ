#Filthy code
#Base 8 -> 자릿수 8^(n)
val=['-','\\','(','@','?','>','&','%']
while (True):
	buf=input()
#	print(f"Buffer: {buf}")
	if buf=='#': break
	k=len(buf)-1
#	print(f"Buffer max exponent: {k}")
	s=0
	for i in range(0,len(buf)):
		if buf[i]=='/':
			s+=(8**k)*(-1)
#			print(f"(8**{k})*(-1)={(8**k)*(-1)}")
			k-=1	
			continue
		for j in range(0,8):	
			if buf[i]==val[j]: 
				s+=(8**k)*j
#				print(f"(8**{k})*{j}={(8**k)*j}")
				break
		k-=1
	print(s)
