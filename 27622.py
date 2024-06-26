#Sussy baka
#ඞ
n=int(input())
log=list(map(int,input().split()))
users=[]
sus=0
for x in log:
    if x>0: 
        users.append(x)
        continue
    elif x<0 and (abs(x) not in users): sus+=1
print(sus)