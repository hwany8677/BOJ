#시간초과나옴
from sys import stdin
stick=[]
for _ in range(int(input())): stick.append(int(stdin.readline()))
face=stick[len(stick)-1]
count=1
# print(f"Max = {max(stick)}")
for i in range(len(stick)-1,-1,-1): 
    if stick[i]>face:
        count+=1
        face=stick[i]
        if stick[i]==max(stick): break
print(count)