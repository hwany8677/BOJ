#Too much for what is required
input=open(0).readline
buf=input().rstrip().split()
pref,dist=buf[1],int(buf[2])
if pref=='FM': pref='MF'
n=int(input())
users=dict()
matchlist=[]
for _ in range(n):
    buf=input().rstrip().split()
    name,gender,d=buf[0],buf[1],int(buf[2])
    if name not in users: users[name]=1
    if (gender==pref or pref=='MF') and d<=dist: 
        if name not in matchlist: matchlist.append(name)
        else: users[name]+=1
matchlist.sort()
if len(matchlist)==0: print("No one yet")
else:
    for match in matchlist:
        for _ in range(users[match]): print(match)
