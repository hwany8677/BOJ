#2*10^5안에 다 돔
n,k=map(int,input().split())
course=list(map(int,input().split()))
course+=reversed(course)
sigma=sum(course)
res=0
i=0
direction=0 #0: 증가, 1: 감소 
while(not(direction) or i>=0):
    k-=course[i]
    if k<=0:
        if k<0:
            if direction: res=i
            else: res=i+1
            break
        elif k==0:
            if direction: res=i
            else: res=i+2 if i!=n-1 else i+1
            break
    if i==n-1: 
        direction=1
        continue
    if direction: i-=1
    else: i+=1
print(res)
