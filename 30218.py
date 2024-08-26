from sys import stdin
input=stdin.readline

# def order(od, s):
#     zp=zip(s, od)
#     res=[x for _, x in sorted(zp)]
#     return res

# def Sn_special(lisT,size):
#     res=[]
#     sigma=[(i+1)*lisT[i] for i in range(size)]
#     res.append(sum(sigma))
#     for j in range(1,len(lisT)-size+1):
#         sigma=[(k+1)*lisT[i] for i,k in zip(range(j,j+size),range(size))]
#         res.append(sum(sigma))
#     return res

def Sn_rewrite(lisT,size):
    res=[]
    for i in range(len(lisT)-size+1):
        sigma=0
        weight=1
        for j in range(i,i+size): 
            sigma+=weight*lisT[j]
            weight+=1
        res.append((sigma,i+1))
    return res

n,k=map(int,input().split())
buf=[]
# od=[i+1 for i in range(n-k+1)]
for _ in range(n): buf.append(int(input()))
# s=Sn_special(buf,k)
s=Sn_rewrite(buf,k)
# od=order(od,s)
s.sort()
for i in range(len(s)):
    print(s[i][1],s[i][0])