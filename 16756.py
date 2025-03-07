n=int(input())
A=list(map(int,input().split()))
mn=A[1]-A[0]
mn=mn if mn>0 else -mn
for i in range(n-1):
    temp=A[i+1]-A[i]
    temp=temp if temp>0 else -temp
    if temp<mn: mn=temp
print(mn)