#Slower, 732ms
from sys import stdin
input=stdin.readline
for _ in range(int(input())):
    s=input().split()
    for i in range(len(s)):
        for j in range(len(s[i])-1,-1,-1):
            print(s[i][j],end='')
        print(' ',end='')
    print()