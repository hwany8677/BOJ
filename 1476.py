#브루트포스?
e,s,m=map(int,input().split())
E,S,M=0,0,0
yr=0
while(1):
    E+=1
    if E>15: E=1
    S+=1
    if S>28: S=1
    M+=1
    if M>19: M=1
    yr+=1
    if e==E and s==S and m==M: break
print(yr)
