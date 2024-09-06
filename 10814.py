from sys import stdin
input=stdin.readline

age=[[] for _ in range(201)]
for _ in range(int(input())):
    ag,name=input().split()
    ag=int(ag)
    age[ag].append(name)
for i in range(1,201): 
    if len(age[i])==0: continue
    for j in range(len(age[i])):
        print(i,age[i][j])