while (True):
	buf=input()
	s=buf[0]
	if s=='#': break
	c=0
	for i in range(2,len(buf)): 
		if ord(buf[i])==ord(s) or ord(buf[i])==ord(s)-32: c+=1
	print(f"{s} {c}")
