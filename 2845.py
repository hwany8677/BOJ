from sys import stdin
input=stdin.readline
Lj,P=map(int,input().split())
ppl=Lj*P
buf=list(map(int,input().split()))
for num in buf:
    print(num-ppl,'',end='')
