target="CAMBRIDGE"
s=input()
for i in s:
	a=True
	for j in target:
		if i==j:
			a=False
			break
	if a: print(i,end='')
