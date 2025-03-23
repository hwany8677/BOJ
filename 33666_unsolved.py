#m개의 메시지가 준비된 상태에서 맨션을 (m*2)개 이상 받으면 -> -1
#단, (m*2)<=avg이어야함.
#시작지점을 이분탐색으로 찾아야 하나?
n,m=map(int,input().split())
p=list(map(int,input().split()))
p.sort()
max_p=p[n-1]
avg=sum(p)/n if max_p>=2 else 0
if (m*2)<=avg:
    if max_p>=m*2:
        print(-1)
        exit(0)
total=[0 for _ in range(m+1)]
for mention in p:
    i=1
    if mention>avg: 
        total[i]+=1
        print(i,'',end='')
    else:
        for _ in range(mention):
            total[i]+=1
            print(i,'',end='')
            i+=1
            if i>m: i=1
    print()
for i in range(1,m+1): print(total[i],'',end='')
print()