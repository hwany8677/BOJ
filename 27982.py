#큐브 크기 = 1x1x1 (M과 N의 조건으로 추론가능)
#6개의 조건을 모두 만족해야 하나의 경우의 수가 됨
from sys import stdin
input=stdin.readline

n,m=map(int,input().split()) #n^3에 m개의 큐브가 존재
n3=n**3
occupied=[[[0 for _ in range(n+2)] for _ in range(n+2)] for _ in range(n+2)]
cubelist=[]
count=0
for _ in range(m):
    i,j,k=map(int,input().split())
    #(i-1,j,k), (i+1,j,k)
    #(i,j-1,k), (i,j+1,k)
    #(i,j,k-1), (i,j,k+1)
    cubelist.append((i,j,k))
    occupied[i][j][k]=1
for idx in range(len(cubelist)):
    i,j,k=map(int,cubelist[idx])
    if occupied[i-1][j][k]<1: continue
    if occupied[i][j-1][k]<1: continue
    if occupied[i][j][k-1]<1: continue
    if occupied[i+1][j][k]<1: continue
    if occupied[i][j+1][k]<1: continue
    if occupied[i][j][k+1]<1: continue
    count+=1
print(count)
