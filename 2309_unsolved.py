#Quick? Nah I'd bubble
h=[]
for i in range(0,9): h.append(int(input()))
for i in range(0,9):
	for j in range(0,8):
		if h[j]>=h[j+1]: h[j],h[j+1]=h[j+1],h[j]
s=0
print(h)
for i in range(0,8): print(h[i])

