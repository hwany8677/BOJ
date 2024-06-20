n=int(input())
fprime1=0
for _ in range(n):
    co,exp=map(int,input().split())
    fprime1+=co*exp
print(fprime1)