#Filthy code (skewed code)
#Greedy...
from math import floor,sqrt
sieve=[i for i in range(0,4000001)]
for i in range(2,floor(sqrt(4000001))+1):
    if sieve[i]==0: continue
    for j in range(i+i,4000001,i):
        if sieve[j]%i==0:
            sieve[j]=0
sieve=sorted(set(sieve))
sieve.remove(0)
sieve.remove(1)
sieve.append(4000001)
n=int(input())
s=0 #sum
c=0 #count
cArchive=[]
startingPoint=0
sieveLen=len(sieve)
while(1):
    # if startingPoint>250000: print(f"startingPoint: {startingPoint}")
    for i in range(startingPoint,sieveLen):
        s+=sieve[i]
        #판단 후 c에 1을 더할지 결정 
        if s>n:
            startingPoint+=1
            s,c=0,0
            # print("Sum limit exceeded")
            break
        if s==n:
            c+=1
            cArchive.append(c)
            startingPoint+=1
            # print("Appended!")
            s,c=0,0
            break
        c+=1
    # print("Anyone...?")
    if sieve[startingPoint]>n:
        print(len(cArchive))
        exit(0)