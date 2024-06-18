#행렬 좀 복습해...
#두 행렬(=벡터) 덧셈이 성립하려면 행과 열의 크기가 같아야 한다.
n,m=map(int,input().split())
A=[]
B=[]
for i in range(n): A.append(list(map(int,input().split())))
for i in range(n): B.append(list(map(int,input().split())))
for i in range(n): 
  for j in range(m):
    print("{} ".format(A[i][j]+B[i][j]),end='')
  print()