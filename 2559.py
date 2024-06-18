#List slicing -> takes O(k) time complexity when len(sublist)=k
n,k=map(int,input().split())
buf=list(map(int,input().split()))
sigma=[]
for i in range(n-k+1): sigma.append(sum(buf[i:i+k]))
print(max(sigma))