#O(n)
n=int(input())
arr=input().split()
p=n
for i in range(0,n):
	if arr[i]=='1':
		p-=1
		continue
	for j in range(2,int(arr[i])): #ex) 10이면 2~9까지 다 대입
		if int(arr[i])%j==0:
			p-=1
			break
print(p)
