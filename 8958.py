t=int(input())
for i in range(0,t):
    s=input()
    sc=0
    stk=0
    for j in s:
        if j=='O': 
            stk+=1
            sc+=stk
        else: stk=0
    print(sc)