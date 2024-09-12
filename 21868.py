#delta=epsilon/coefficient
ep_numer,ep_denomi=map(int,input().split())
s=list(map(int,input().split()))
x=s[0]
const=s[1] 
x0=int(input())
L=x*x0+const
print(L) 
ep_numer*=(ep_denomi)*L
if ep_numer>10**8 or x==0: print(0,0)
else: print(ep_numer,ep_denomi)