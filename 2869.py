a,b,v=map(int,input().split())
delta=a-b
days=v//delta
if days*delta==v:
    if (days*delta)-delta+a>v: days-=1
    else: days-=1
elif days*delta<v: days+=1
elif days*delta>v: days-=1
print(days)