o,i=0,0
cur=0
max=0
for i in range(0,4):
	o,i=map(int,input().split())
	cur=cur+i-o
	if max<cur: max=cur
print(max)
