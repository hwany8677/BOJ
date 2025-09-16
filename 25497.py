#L-R, S-K
input=open(0).readline
n=int(input())
skills=input().rstrip()
c=0
lr_start,sk_start=0,0
for i in range(n):
    skill=skills[i]
    if skill.isnumeric(): c+=1
    elif skill=='L':
        #if sk_start>0: sk_start=0 
        lr_start+=1
    elif skill=='R':
        if lr_start==0: break
        if lr_start>0:
            lr_start-=1
            c+=1
    elif skill=='S': 
        #if lr_start>0: lr_start=0
        sk_start+=1
    elif skill=='K':
        if sk_start==0: break
        if sk_start>0:
            sk_start-=1
            c+=1
print(c)
