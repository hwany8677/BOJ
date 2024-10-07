#Another day, another brute-forcing
n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
x.sort()
y.sort()
does_exist=True
for wand in x:
    to_continue=False
    i=0
    while(i<n):
        if y[i]>=wand: 
            to_continue=True
            y[i]=-1
            break
        i+=1
    if to_continue: continue
    else: does_exist=False
if does_exist: print("DA")
else: print("NE")
