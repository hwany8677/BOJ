#Reminds me of insertion sort...
input=open(0).readline
n,m=map(int,input().split())
buf=[i for i in range(n+1)]
for _ in range(m):
    i,j=input().split()
    i=int(i.strip("T"))
    j=int(j.strip("T"))
    if buf.index(i)>buf.index(j):
        start=buf.index(j)
        end=buf.index(i)
        temp=buf[start]
        for k in range(start,end): buf[k]=buf[k+1]
        buf[end]=temp
for i in range(1,n+1): print(f"T{buf[i]} ",end='')
print(c)
