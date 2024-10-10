#(x-k)*n=x
#x-k=x/n
#x=(x/n)+k
#x*(1-(1/n))=k, 1-(1/n) = (n-1)/n
#x=k*(n/(n-1)) << ZeroDivisionError??
k,n=map(int,input().split())
if n==1: 
    print(-1)
    exit(0)
res=int(k*n//(n-1))
res+=1 if (k*n%(n-1)) else 0 
print(res)
