#Sliding window
n,x=map(int,input().split())
visits=list(map(int,input().split()))
start,end=0,x-1
window=[visits[i] for i in range(end+1)]
start+=1; end+=1
mx_sum=sum(window); mx_count=1
while(end<len(visits)):
    window.pop(0)
    window.append(visits[end])
    sigma=sum(window)
    if sigma>mx_sum: 
        mx_sum=sigma
        mx_count=1
    elif sigma==mx_sum:
        mx_count+=1
    end+=1
print(f"{mx_sum}\n{mx_count}" if mx_sum!=0 else "SAD")