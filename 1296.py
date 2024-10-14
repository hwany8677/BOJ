input=open(0).readline
name=input().rstrip()
love_c=[0,0,0,0]
for char in name:
    if char=='L': love_c[0]+=1
    elif char=='O': love_c[1]+=1
    elif char=='V': love_c[2]+=1
    elif char=='E': love_c[3]+=1
mn=-1
res=''
#print(love_c)
n=int(input())
buf=[]
for _ in range(n): buf.append(input().rstrip())
buf.sort()
for i in range(n):
    love=love_c[:]
    s=buf[i]
    #print(s)
    for char in s:
        if char=='L': love[0]+=1
        elif char=='O': love[1]+=1
        elif char=='V': love[2]+=1
        elif char=='E': love[3]+=1
    L,O,V,E=love[0],love[1],love[2],love[3]
    #print(love)
    prob=((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E))%100
    #print(f"prob={prob}")
    if prob>mn:
        mn=prob
        res=s
print(res)
