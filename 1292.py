#Nai?ve
start,end=map(int,input().split())
sigma=0
lisT=[]
for i in range(1,int(end/2)+2):
    for _ in range(i): lisT.append(i)
for i in range(start-1,end):
    sigma+=lisT[i]
print(sigma)