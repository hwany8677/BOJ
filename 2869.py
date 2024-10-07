a,b,v=map(int,input().split())
#Day 1 pre-exit
if a==v:
    print(1)
    exit(0)
delta=a-b
days=1
v-=a
days+=(v//delta)
if v%delta>0: days+=1
print(days)
