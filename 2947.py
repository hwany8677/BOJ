#버블정렬을 설명한 글
s=list(map(int,input().split()))
for i in range(0,5):
	for j in range(1,5):
		if s[j-1]>s[j]:
			s[j-1],s[j]=s[j],s[j-1]
			for k in s: print(f"{k} ",end='')
			print()

