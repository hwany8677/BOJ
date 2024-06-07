n=int(input())
B=list(map(int,input().split()))
A=[]
prevSum=0
for i in range(len(B)):
    A.append((i+1)*B[i]-prevSum)
    prevSum+=A[i]
print(*(A))