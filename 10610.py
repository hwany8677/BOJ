#이게 뭐라고 3시간 이상을...
#he wants to know the *****maximum***** multiple of the number 30
#						^^^^^^^^^^^^ 저걸못봤다고???????
def div(n):
    for _ in range(zero): n.remove(0)
    n.sort()
    n.reverse()
    for _ in range(zero): n.append(0)
    n=list(map(str,n))
    s=""
    for c in n: s+=c
    n=int(s)
    return n
n=list(map(int,input()))
zero=0
for i in n: zero+=1 if i==0 else 0
if zero==0: 
    print(-1)
else:
#    rvs_n=list(n)
#    rvs_n.reverse()
    n=div(n)
#    rvs_n=div(rvs_n)
    if n%30==0: print(n)
#    elif rvs_n%30==0: print(rvs_n)
    else: print(-1)