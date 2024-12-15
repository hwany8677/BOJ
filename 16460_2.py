input=open(0).readline
buf=input().rstrip().split()
pref,dist=buf[1],int(buf[2])
n=int(input())
matchlist=[]
for _ in range(n):
    name,gender,d=input().rstrip().split()
    d=int(d)
    if (gender in pref) and d<=dist: matchlist.append(name)
matchlist.sort()
if len(matchlist)==0: print("No one yet")
else:
    for names in matchlist: print(names)
