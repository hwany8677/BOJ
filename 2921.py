#가능한 모든 경우의 수.
n=int(input())
s=0
for i in range(0,n+1):
    for j in range(i,n+1):
        s+=i+j
print(s)