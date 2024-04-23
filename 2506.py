#1: O 0: X
n=int(input())
s=input().split()
sum=0
streak=0
if int(s[0]): 
    sum+=1
    streak+=1
for i in range(1,n):
    if int(s[i]):
        streak+=1
        sum+=streak
    else: streak=0
print(sum)