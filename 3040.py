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
			print(f"Current probe state: {probe}")
			s=add(probe,dw)
			print(f"Probe's sum = {s}")	
			if s==100: 
				print("Match found!")
				return probe
			else: 
				probe[i]+=1
		print()
dw=[]
for _ in range(0,9): dw.append(int(input()))
print(f"Drawfs: {dw}")
probe=calc(dw)
for n in probe: print(n)
