#164ms
from sys import stdin
input=stdin.readline
for _ in range(int(input())):
    s=input().split()
    for i in range(len(s)):
        s[i]=list(s[i])
        s[i].reverse()
        s[i]=''.join(s[i])
    print(*s)