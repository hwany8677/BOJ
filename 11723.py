#try-except is not recommended
#Took 5480ms
from sys import stdin
input=stdin.readline
seT=[0 for _ in range(21)] #0번은 공백
m=int(input())
for _ in range(m):
    s=input().rstrip()
    #느리게 하는 원인 (추정)
    try: 
        cmd,x=s.split()
        x=int(x)
    except ValueError: cmd=s
    if cmd=="toggle": seT[x]=0 if seT[x] else 1
    if cmd=="add": seT[x]=1
    if cmd=="remove": seT[x]=0
    if cmd=="check": print(seT[x])
    if cmd=="all": seT=[1 for _ in range(21)]
    if cmd=="empty": seT=[0 for _ in range(21)]
