#Array spam
#Not sure if this is a good idea to be very honest
from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
points=list(map(int,input().split()))
info_st=[]
info_sc=[]
for i in range(m):
    buf=input().split()
    sigma=0
    for j in range(1,n+1):
        if buf[j]=='O': sigma+=points[j-1]
        else: sigma+=0
    info_st.append(int(buf[0]))
    info_sc.append(sigma)
mx=max(info_sc)
dupe_list=[]
for i in range(m):
    if info_sc[i]==mx:
        dupe_list.append(info_st[i])
print(min(dupe_list),mx)