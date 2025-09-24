n=int(input())
while(not(n==0)):
    mid=25
    low,high=1,50
    while(not(mid==n)):
        print(mid,end=' ')
        if not(mid==n): 
            if mid>n: high=mid-1
            elif mid<n: low=mid+1
            mid=(low+high)//2
    if mid==n: print(mid)
    n=int(input())