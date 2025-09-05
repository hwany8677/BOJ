#애라 모르겠다 적은게 답이지 뭐
def search(n,lane): #Only if n!=1
    diff,passes=0,1
    current=1
    to_add=lane-1
    while(current<n):
        current+=to_add
        to_add+=6
        passes+=1
    diff=current-n
    #return (diff,passes,current) #(시도가 있었던 흔적)
    return passes
n=int(input())
#2,3,4,5,6,7
res=[]
for i in range(2,8): res.append(search(n,i))
res.sort()
print(res[0])
