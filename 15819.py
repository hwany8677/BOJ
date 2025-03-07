#0~9, a~z, 짧은 순
input=open(0).readline
n,i=map(int,input().split())
handle=[]
for _ in range(n): handle.append(input().rstrip())
handle.sort()
print(handle[i-1])