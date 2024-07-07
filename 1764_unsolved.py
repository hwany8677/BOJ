#TLE
n,m=map(int,input().split())
DBS=[]
for _ in range(n):
    DBS.append(input())
BMS=[]
count=0
for _ in range(m):
    s=input()
    if s in DBS: 
        BMS.append(s)
        count+=1
print(count)
for element in BMS:
    print(element)