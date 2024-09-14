#피보나치같은 피보나치같지않은
#수 작으니 선형으로 계산
n=int(input())
a,b,c=1,1,1
if n<4: print(1); exit(0)
temp=0
for i in range(n-3):
    temp=a+c
    a,b,c=b,c,temp
print(temp)