from sys import stdin
input=stdin.readline
for i in range(int(input())):
    buf=list(map(int,input().split()))
    print(f"Case #{i+1}: {max(buf)}")