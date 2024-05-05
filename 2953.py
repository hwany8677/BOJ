s=[]
max=0
for i in range(0,5): s.append(list(map(int,input().split())))
for i in range(0,5):
	if sum(s[i])>=sum(s[max]): max=i
print(max+1,sum(s[max])) 
