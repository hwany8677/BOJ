#순위구현이 세상에서 제일 싫다
from sys import stdin
input=stdin.readline

n=int(input())
scoreboard=[0 for i in range(n+1)]
order=[0 for i in range(1,n+1)]
for i in range(int(((n)*(n-1) /2))):
    a,b,res_a,res_b=map(int,input().split())
    scoreboard[a]+=3 if res_a>res_b else 1 if res_a==res_b else 0
    scoreboard[b]+=3 if res_b>res_a else 1 if res_a==res_b else 0
scoreboard.pop(0)
sc=sorted(set(scoreboard))
sc.reverse()
pos=1
for score in sc:
    has_dupes=-1
    for i in range(len(scoreboard)):
        if scoreboard[i]==score:
            order[i]=pos
            has_dupes+=1
    pos+=(has_dupes+1)
for od in order: print(od)