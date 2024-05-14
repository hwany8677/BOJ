#Brute-Force Algo
def add(probe,dw):
	s=0
	for i in range(0,7):
		s+=dw[probe[i]]
	return s
def calc(dw):
	probe=[0,1,2,3,4,5,6]
	for i in range(6,-1,-1):
		for j in range(0,2):
			s=add(probe,dw)	
			if s==100: return probe
			else: probe[i]+=1
	return probe
dw=[]
for _ in range(0,9): dw.append(int(input()))
probe=calc(dw)
for n in probe: print(n)
