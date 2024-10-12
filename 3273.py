n=int(input())
buf=list(map(int,input().split()))
to_find=int(input())
buf.sort()
count=0
start=0
end=n-1
while(start<end):
    sigma=buf[start]+buf[end]
    if sigma==to_find:
        count+=1
        start+=1
    elif sigma>to_find: end-=1
    elif sigma<to_find: start+=1
print(count)