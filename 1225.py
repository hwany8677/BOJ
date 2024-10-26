#a를 기준으로 계산
a,b=input().split()
b=[int(digit) for digit in b]
b=sum(b)
res=0
for digit in a: res+=int(digit)*b
print(res)
