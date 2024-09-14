#귀찮아
from sys import stdin
input=stdin.readline

buf=[]
for _ in range(int(input())): buf.append(int(input()))
buf.sort()
for num in buf: print(num)