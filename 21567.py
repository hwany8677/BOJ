#파이썬으로 시간초과나면 C로
a=int(input())
b=int(input())
c=int(input())
res=list(str(int(a*b*c)))
count=[0 for _ in range(10)]
for i in res: count[int(i)]+=1
for i in count: print(i)