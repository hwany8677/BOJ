#"입력으로 주어지는 S에 해당하는 수열 A는 항상 유일하다."
#=입력은 수열 A가 형성되게끔 딱 주어진다는 소리
#수를 가지고 노는 건 아직 무리...
input=open(0).readline
n=int(input())
buf=[]
A=[]
for _ in range(n): buf.append(list(map(int,input().split())))
if n==2:
    print(1,1)
    exit(0)
for i in range(n-2):
    apb=buf[i][i+1]
    amb=buf[i][n-1]-buf[i+1][n-1]
    a=(apb+amb)//2
    b=apb-a
    A.append(a)
A.append(b)
A.append(buf[n-2][n-1]-b)
print(*A)