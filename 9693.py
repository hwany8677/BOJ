#5의 배수를 지날 때 마다 기본 자릿수가 증가
input=open(0).readline
precalc=[5,25,125,625,3125,15625,78125,390625]
n=int(input())
i=1
while(n!=0):
    zero_trail=0
    for div in precalc:
    zero_trail+=n//div
    print(f"Case #{i}: {zero_trail}")
    n=int(input())
    i+=1
