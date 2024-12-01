p1=list(map(int,input().split()))
p2=list(map(int,input().split()))
wins=0
cases=0
for die1 in p1:
    for die2 in p2:
        if die1>die2: wins+=1
        if die1!=die2: cases+=1
print("{:.5f}".format(wins/cases))