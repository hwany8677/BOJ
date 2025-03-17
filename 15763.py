#Refactor needed
#Cow's names: A...Z
#2마리의 소가 팀을 맺는 경우만 브루트포스 돌리기
row=[]
names=[]
for _ in range(3): row.append(input().rstrip())
for i in range(3):
    for j in range(3): 
        if row[i][j] not in names: names.append(row[i][j])
#수직 수평 대각 확인
#1. 수평, 2. 수직, 3. (0,0), (2,0)에서 x자로 확인
wins=[]
tictactoe=0
for i in range(3):
    first_letter=row[i][0]
    combo=1
    for j in range(1,3):
        if row[i][j]==first_letter: combo+=1
    if combo==3: 
        if first_letter not in wins: 
            wins.append(first_letter)
            tictactoe+=1
for j in range(3):
    first_letter=row[0][j]
    combo=1
    for i in range(1,3):
        if row[i][j]==first_letter: combo+=1
    if combo==3: 
        if first_letter not in wins:
            wins.append(first_letter)
            tictactoe+=1
if row[0][0]==row[1][1]==row[2][2]: 
    if row[0][0] not in wins:
        wins.append(row[0][0])
        tictactoe+=1
if row[2][0]==row[1][1]==row[0][2]: 
    if row[1][1] not in wins:
        wins.append(row[1][1])
        tictactoe+=1
print(tictactoe)
#팀전 경우의수 브포
tictactoe=0
wins=[]
for t1 in range(len(names)):
    for t2 in range(t1,len(names)):
        cow1=names[t1]
        cow2=names[t2]
        if cow1==cow2: continue
        #print(cow1,cow2)
        #수평
        for i in range(3):
            combo=0
            c1,c2=False,False
            for j in range(3):
                if row[i][j]==cow1:
                    c1=True
                    combo+=1
                if row[i][j]==cow2: 
                    c2=True
                    combo+=1
            if combo==3 and c1 and c2: 
                #print("ROW TIC")
                if (cow1,cow2) not in wins:
                    wins.append((cow1,cow2))
                    tictactoe+=1
        #수직
        for j in range(3):
            combo=0
            c1,c2=False,False
            for i in range(3):
                if row[i][j]==cow1:
                    c1=True
                    combo+=1
                if row[i][j]==cow2: 
                    c2=True
                    combo+=1
            if combo==3 and c1 and c2: 
                #print("COL TIC")
                if (cow1,cow2) not in wins:
                    wins.append((cow1,cow2))
                    tictactoe+=1
        #대각선
        combo=0
        c1,c2=False,False
        for i in range(3):
            if row[i][i]==cow1:
                c1=True
                combo+=1
            if row[i][i]==cow2: 
                c2=True
                combo+=1
        if combo==3 and c1 and c2: 
            #print("DIAG TIC 1")
            if (cow1,cow2) not in wins:
                wins.append((cow1,cow2))
                tictactoe+=1
        combo=0
        c1,c2=False,False
        for i in range(3):
            if row[2-i][i]==cow1:
                c1=True
                combo+=1
            if row[2-i][i]==cow2: 
                c2=True
                combo+=1
        if combo==3 and c1 and c2: 
            #print("DIAG TIC 2")
            if (cow1,cow2) not in wins:
                wins.append((cow1,cow2))
                tictactoe+=1
        #print(f"tictactoe={tictactoe}")
print(tictactoe)
