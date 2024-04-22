n=int(input())
left=0
for i in range(0,n):
    s,a=map(int,input().split())
    left+=a-s*(a//s)
print(left)