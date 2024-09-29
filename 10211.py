from sys import stdin
input=stdin.readline

def Sn(lisT,n):
    res=[lisT[0]]
    for i in range(1,n): res.append(lisT[i]+res[i-1])
    return res
def search(lisT,n):
    #window=1 -> 1개의 원소만
    #window=2 -> Sn-S(n-1) = 2개의 원소가 연속으로
    window=2
    mx=-1001
    while(window<=n):
        mx=lisT[window-1] if lisT[window-1]>mx else mx
        for i in range(n-window):
            temp=lisT[i+window]-lisT[i]
            if temp>mx: mx=temp
        window+=1
    return mx
for _ in range(int(input())):
    n=int(input())
    buf=list(map(int,input().split()))
    sums=Sn(buf,n)
    mx=max(buf)
    temp=search(sums,n)
    mx=temp if temp>mx else mx
    print(mx)