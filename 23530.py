from sys import stdin
from random import randint as r
for _ in range(int(input())):
    a,b=map(int,stdin.readline().split())
    sol=a+b
    while(sol==a+b): sol=r(1,50)
    print(sol)