d1=sorted(list(map(int,input().split())))
d2=sorted(list(map(int,input().split())))
count=0
for num1 in d1:
    for num2 in d2:
        if num1>num2: count+=1
bunja=count
bunmo=36
c=2
while(c<20): #gcd쓰기귀찮음
    if bunja%c==0 and bunmo%c==0: 
        bunja//=c
        bunmo//=c
        continue
    c+=1
print(f"{bunja}/{bunmo}" if bunja!=bunmo else "1")