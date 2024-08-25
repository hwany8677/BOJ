from sys import stdin
input=stdin.readline

def order(lisT1, lisT2):
    zp=zip(lisT2, lisT1)
    res=[x for _, x in sorted(zp)]
    return res

def Sn(lisT):
    global od
    c=2
    res=[lisT[0]]
    od.append(1)
    for i in range(1,len(lisT)):
        res.append(lisT[i]+res[i-1])
        od.append(c)
        c+=1
    return res

def Sn_special(lisT,size):
    global od
    res=[]
    sigma=[(i+1)*lisT[i] for i in range(size)]
    res.append(sum(sigma))
    c=2
    od.append(1)
    for j in range(size-1,len(lisT)-1):
        sigma=[lisT[i] for i in range(j-1,j+size-1)]
        for k in range(size): sigma[k]=(k+1)*sigma[k]
        res.append(sum(sigma))
        od.append(c)
        c+=1
    return res

n,k=map(int,input().split())
buf=[]
od=[]
for _ in range(n):
    buf.append(int(input()))
s=Sn(buf) if k==1 else Sn_special(buf,k)
od=order(od,s)
s.sort()
for i in range(len(s)):
    print(od[i],s[i])