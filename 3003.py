#1 1 2 2 2 8
chess=list(map(int,input().split()))
chess2=[1,1,2,2,2,8]
for i in range(6): print(chess2[i]-chess[i],end=' ')
print()