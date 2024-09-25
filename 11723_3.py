from sys import stdin
input=stdin.readline
seT=[False]*21
m=int(input())
for _ in range(m):
    s=input().rstrip().split()
    cmd=s[0]
    if len(s)==2: x=int(s[1])
    if cmd=="toggle": seT[x]=False if seT[x] else True
    if cmd=="add": seT[x]=True
    if cmd=="remove": seT[x]=False
    if cmd=="check": print(int(seT[x]))
    if cmd=="all": seT=[True]*21
    if cmd=="empty": seT=[False]*21
