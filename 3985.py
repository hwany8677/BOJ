input=open(0).readline
l=int(input())
n=int(input())
roll=[1 for _ in range(l+1)]
mx_expected,exp_id=0,0
mx_actual,res_id=0,0
for i in range(n):
    a,b=map(int,input().split())
    if b-a+1>mx_expected: 
        mx_expected=b-a+1
        exp_id=i+1
    count=0
    for j in range(a,b+1):
        if roll[j]==1: 
            roll[j]=0
            count+=1
    if count>mx_actual: mx_actual,res_id=count,i+1
print(exp_id)
print(res_id)
