n,t=map(int,input().split())
task=list(map(int,input().split()))
s,c=0,0
for i in task:
    s+=i
    if s>t: break
    else: c+=1
print(c)