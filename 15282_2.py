#좀 더 빠르게는 안되나?
n,m=map(int,input().split())
t=list(map(int,input().split()))
l=list(map(int,input().split()))
t.sort(reverse=True)
l.sort(reverse=True)
c=0
lt,ll=len(t),len(l)
while(lt>0 and ll>0):
    ti=t[lt-1]
    li=l[ll-1]
    if ti<=li: lt,ll,c=lt-1,ll-1,c+1
    elif ti>li: ll-=1
print(c)
    
