#A = [2, 3, 1]
#A[0]=2, A[1]=3, A[2]=1
#B[0]=1=A[2], B[1]=2=A[0], B[2]=3=A[1]
#->P[0]=1, P[1]=2, P[2]=0
#원래 A를 가리키는 인덱스 수열이 필요
n=int(input())
a=list(map(int,input().split()))
a_idx=[i for i in range(n)]
b=sorted(a)
zipper=list(zip(a_idx,a))
zipper.sort(key=lambda x:x[1])
for i in range(n): a_idx[i]=zipper[i][0]
p=[0 for _ in range(n)]
for i in range(n): p[a_idx[i]]=i
print(*p)
