n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
s=0
A.sort()
B.sort(reverse=True)
for i in range(n): s+=A[i]*B[i]
print(s)