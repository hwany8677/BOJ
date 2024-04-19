a,d=100,100
t=int(input())
for i in range(0,t):
    an,da=map(int, input().split())
    if an>da: d-=an
    elif an<da: a-=da
print(f"{a}\n{d}")