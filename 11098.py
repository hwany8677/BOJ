n=int(input())
for i in range(0,n):
	player=[]
	price=[]
	max=0
	p=int(input())
	for j in range(0,p):
		buf=input().split()
		price.append(int(buf[0]))
		player.append(buf[1])
		if price[max]<price[j]: max=j
	print(player[max])
