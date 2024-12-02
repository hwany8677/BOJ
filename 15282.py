#180 160 150 100 100
#190 170 160 140
#Ans: 4 (100,140), (150,160), (160,170), (180,190)
#-> t_i 에 해당하는 l_i가 없을 시 pop하고 넘어가기
#t_i<=l_i 이면 양쪽 다 pop, t_i>l_i 이면 l_i를 pop
#199 185 180 100
#199 180 170 120
#Ans: 3 (100,120), (180,180), (185,199)
n,m=map(int,input().split())
t=list(map(int,input().split()))
l=list(map(int,input().split()))
t.sort(reverse=True)
l.sort(reverse=True)
count=0
while(len(t)>0 and len(l)>0):
    t_i=t[len(t)-1]
    l_i=l[len(l)-1]
    if t_i<=l_i:
        t.pop()
        l.pop()
        count+=1
    elif t_i>l_i: l.pop()
print(count)
