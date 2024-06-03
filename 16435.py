n,l=map(int,input().split())
h=list(map(int,input().split()))
h.sort() #에이 설마 뭔 일 일어나겠어? (지연시간폭탄)
for food in h:
    if l>=food: l+=1
    else: break
print(l)