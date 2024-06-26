from math import floor,sqrt
sieve=[True]*1005000
sieve[0],sieve[1]=False,False
for i in range(2,floor(sqrt(1005000))+1):
    if sieve[i]==False: continue
    for j in range(i+i,1005000,i):
        if j%i==0:
            sieve[j]=False
n=int(input())
while(1):
    if sieve[n]==False:
        n+=1
        continue
    s=str(n)
    slen=len(s)
    c=0
    for i in range(slen):
        if s[i]==s[slen-1-i]: c+=1
    if c==slen: 
        print(s)
        break
    n+=1