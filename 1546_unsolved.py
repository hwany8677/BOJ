n=int(input())
grade=input().split()
m=0
for i in range(0,len(grade)): 
    grade[i]=int(grade[i])
    if grade[i]>grade[m]: m=i
m=grade[m]
for i in range(0,len(grade)): grade[i]=grade[i]/m*100
print("{:.1f}".format(sum(grade)/n))