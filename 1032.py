n=int(input())
buf=input()
specimen=list(buf)
for _ in range(n):
    temp=buf
    for i in range(len(specimen)):
        if temp[i]!=specimen[i]: specimen[i]='?'
    if _<n-1: buf=input()
print(*specimen,sep='')