from sys import stdin
input=stdin.readline

for _ in range(int(input())):
    buf=list(map(int,input().split()))
    print(min(buf))