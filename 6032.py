input=open(0).readline
n=int(input())
hfm=[]
for i in range(n):
    j,p=map(int,input().split())
    hfm.append((j/p,p,i+1))
hfm.sort(reverse=True)
sigma=0
for i in range(3): sigma+=hfm[i][1]
print(sigma)
for i in range(3): print(hfm[i][2])
