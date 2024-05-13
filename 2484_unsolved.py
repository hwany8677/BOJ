#Filthy code
#Worst code ever (drowsiness for added bonus)
#찾고, 세고, 판단한다.
n=int(input())
dice=[]
for i in range(0,n):
	dice.append(list(map(int,input().split())))
	dice[i].sort()
score=[]
for i in range(0,n):
	maxC=0
	pair=0 #combo=2
	pos1,pos2=0,0
	combo=1
	triM=0 #combo=3
	for j in range(0,3):
		if dice[i][j]==dice[i][j+1]:
			combo+=1
			if pair==1 and combo==2:
				pos2=j
				pair+=1
				break
			if combo==2 and j==2: 
				pos1=j
				pair+=1
		else: #같지않을때
#			if pair==1 and combo==2:
#				pos2=j
#				pair+=1
#				break 
			if combo==3: 
				if dice[i][j]>=triM: triM=dice[i][j]
			if combo==2: 
				pair+=1
				pos1=j
			combo=1
		if combo>=maxC: maxC=combo
	print(f"pos1: {pos1}, pos2: {pos2}")
	print(f"combo={maxC}")
	if maxC==4: score.append(50000+dice[i][0]*5000)
	elif maxC==3: score.append(10000+triM*1000)
	elif maxC==2: 
		if pair==2: score.append(2000+dice[i][pos1]*500+dice[i][pos2]*500)
		elif pair==1: score.append(1000+dice[i][pos1]*100)
	elif maxC==1: score.append(max(dice[i])*100)
print(score)
print(max(score))
