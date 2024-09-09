#3512ms
from sys import stdin
input=stdin.readline
seT=[0 for _ in range(21)] #0번은 공백
m=int(input())
for _ in range(m):
    s=input().rstrip().split()
    cmd=s[0]
    if len(s)==2: x=int(s[1])
    if cmd=="toggle": seT[x]=0 if seT[x] else 1
    if cmd=="add": seT[x]=1
    if cmd=="remove": seT[x]=0
    if cmd=="check": print(seT[x])
    if cmd=="all": seT=[1 for _ in range(21)]
    if cmd=="empty": seT=[0 for _ in range(21)]
