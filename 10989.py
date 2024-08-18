#'다 센다'
from sys import stdin
input=stdin.readline
info=[0 for _ in range(10000+1)]
mx=0
for _ in range(int(input())):
    n=int(input())
    info[n]+=1
    mx=n if n>mx else mx
for i in range(mx+1):
    for j in range(info[i]):
        print(i)