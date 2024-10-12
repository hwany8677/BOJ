#Naive method
input=open(0).readline
for _ in range(int(input())):
    a,b=map(int,input().split())
    num=0 #0번은 10번째 컴퓨터를 의미함
    num=(a**b)%10
    if num==0: print(10)
    else: print(num)
