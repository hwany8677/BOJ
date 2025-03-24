#Using sets
input=open(0).readline
for _ in range(int(input())):
    m=int(input())
    msq=[]
    sigma=set()
    for _ in range(m): msq.append(list(map(int,input().split())))
    for i in range(m): sigma.add(sum(msq[i]))
    for j in range(m):
        sig=0
        for i in range(m): sig+=msq[i][j]
        sigma.add(sig)
    s1,s2=0,0
    for i in range(m): 
        s1+=msq[i][i]
        s2+=msq[m-i-1][i]
    sigma.add(s1)
    sigma.add(s2)
    if len(sigma)==1: print("Magic square of size",m)
    else: print("Not a magic square")
