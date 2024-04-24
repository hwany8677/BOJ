#Bubble bubble
arr=[]
for i in range(0,5): arr.append(int(input()))
for i in range(0,5):
	for j in range(0,4):
		if arr[j]>=arr[j+1]: arr[j],arr[j+1]=arr[j+1],arr[j]
print(int(sum(arr)/5))
print(arr[2])
