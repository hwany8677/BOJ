from sys import stdin
input=stdin.readline
buf=[]
n=int(input())
for _ in range(n):
    buf.append(int(input()))
buf.sort()
for i in range(n):
    print(buf[i])