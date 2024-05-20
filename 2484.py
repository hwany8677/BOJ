#Filthy code
#Nested if-statement
#(idk about you watching this code but I do see a room for improvement)
n=int(input())
pM=[]
for _ in range(0,n):
	dice=list(map(int,input().split()))
	dice.sort()
#  print(dice)
	if dice[0]==dice[1]==dice[2]==dice[3]: # 3 3 3 3
		pM.append(50000+dice[0]*5000)
	elif dice[0]==dice[1]==dice[2] or dice[1]==dice[2]==dice[3]: # 3 3 3 6 or 1 2 2 2
		pM.append(10000+dice[1]*1000)
	elif dice[0]==dice[1]: 
		if dice[2]==dice[3]: # 1 1 2 2
			pM.append(2000+dice[0]*500+dice[2]*500)
		else: pM.append(1000+dice[0]*100) # 1 1 2 3
	elif dice[1]==dice[2] or dice[2]==dice[3]: # 1 2 2 3 or 1 2 3 3
		pM.append(1000+dice[2]*100)
	elif not(dice[0]==dice[1]==dice[2]==dice[3]): # 1 2 3 4
		  pM.append(max(dice)*100)
#print(pM)
print(max(pM))