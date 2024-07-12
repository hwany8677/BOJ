#이진탐색 때릴꺼임
def bin_search(start,end,lisT,target):  
    while(start<=end):
        mid=(start+end)//2
        if lisT[mid]==target: return 1
        elif lisT[mid]<target:
            start=mid+1
        elif lisT[mid]>target:
            end=mid-1
    return 0
n=int(input())
lisT=list(map(int,input().split()))
lisT.sort() 
n_find=int(input())
to_find=list(map(int,input().split()))
start=0
end=n-1
for num in to_find:
    print(bin_search(start,end,lisT,num))