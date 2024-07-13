#List slicing -> takes O(k) time complexity when len(sublist)=k
#sol: cumulative sum
#cumsum
def Sn(lisT):
    res=[lisT[0]]
    for i in range(1,len(lisT)):
        res.append(lisT[i]+res[i-1])
    return res
n,k=map(int,input().split())
buf=list(map(int,input().split()))
if k==1: print(max(buf))
else: #배열을 이미 만들어놓고 왜 또 탐색을 하는거지?
    sigma=Sn(buf)
    mx_sigma=0
    start,end=0,k-1
    while (end<len(buf)):
        if start==0: mx_sigma=sigma[end]
        else:
            temp=sigma[end]-sigma[start-1]
            if temp>mx_sigma: mx_sigma=temp
        start+=1
        end+=1
    print(mx_sigma)