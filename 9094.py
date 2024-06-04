#Fun fact: it takes CPython 4772ms to run
#a, b -> 1~(n-1)까지의 범위를 가짐
from sys import stdin
for _ in range(int(input())):
    n,m=map(int,stdin.readline().split())
    pairs=[]
    for a in range(1,n):
        for b in range(a+1,n):
            buf=(a**2+b**2+m)%(a*b)
            if buf==0: pairs.append((a,b))
    print(len(pairs))