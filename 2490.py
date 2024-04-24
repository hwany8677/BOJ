for i in range(0,3):
	yut=input().split()
	for j in range(len(yut)): yut[j]=int(yut[j])
	if sum(yut)==4: print('E')
	elif sum(yut)==3: print('A')
	elif sum(yut)==2: print('B')
	elif sum(yut)==1: print('C')
	elif sum(yut)==0: print('D') 
