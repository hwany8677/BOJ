#리스트? 그게 먹는건가?
n=int(input())
point=list(map(int,input().split()))
pivot=0
max=0
for i in range(0,len(point)):
	if i+1==len(point) or point[i]>=point[i+1]:
		if point[i]-point[pivot]>=max:
			max=point[i]-point[pivot]
		pivot=i+1
print(max)
