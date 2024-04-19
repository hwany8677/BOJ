# A: 300초 B: 60초 C: 10초
t=int(input())
if t%10: print(-1)
else:  
    bt=[300,60,10]
    pressC=[0,0,0]
    for i in range(0,3):
        if t//bt[i]!=0:
            pressC[i]+=t//bt[i]
            t=t-(t//bt[i])*bt[i] #여기에서 뺄꺼 다 뺌
        else: continue
    for i in pressC: print(f"{i} ",end='')