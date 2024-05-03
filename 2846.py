#왜 자꾸 리스트를 만들려고 하는거지...?
#리스트 없는 알고리즘은 2846_2로
n=int(input())
point=list(map(int,input().split()))
height=[]
pivot=0
max=0
for i in range(0,len(point)):
	if i+1==len(point) or point[i]>=point[i+1]:
		height.append(point[i]-point[pivot])
		pivot=i+1
for i in range(0,len(height)):
	if height[i]>=max: max=height[i]
print(max)
