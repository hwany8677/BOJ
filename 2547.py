from sys import stdin
input=stdin.readline

for _ in range(int(input())):
    input()
    n=int(input())
    sigma=0
    for _ in range(n):
        sigma+=int(input())
    if sigma%n==0: print("YES")
    else: print("NO")