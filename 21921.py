#구간합
def Sn(lisT):
    S=[lisT[0]]
    for i in range(1,len(lisT)):
        S.append(lisT[i]+S[i-1])
    return S
n,x=map(int,input().split())
visits=list(map(int,input().split()))
start,end=0,x-1
s=Sn(visits)
mx_sum=0 #기간 內 최대 방문자 수
mx_count=0 #==mx_sum
while(end<len(visits)):
    if start==0: sigma=s[end]
    else: sigma=s[end]-s[start-1]
    if sigma>mx_sum: 
        mx_sum=sigma
        mx_count=1
    elif sigma==mx_sum:
        mx_count+=1
    start+=1
    end+=1
print(f"{mx_sum}\n{mx_count}" if mx_sum!=0 else "SAD")