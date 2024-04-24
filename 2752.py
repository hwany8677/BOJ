#Bubble
arr=input().split()
for i in range(0,3): arr[i]=int(arr[i])
for i in range(0,2):
	for j in range(0,2):
		if arr[j]>=arr[j+1]:
			arr[j],arr[j+1]=arr[j+1],arr[j]
for i in arr: print(f"{i} ",end='')
