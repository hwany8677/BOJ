global real_res
def exp(n):
    if n>1:
        exp_input=n%2
        if exp_input:
            res1=exp(n//2)
            res2=exp(n//2+1)
            temp=res1*res2
            real_res.append(temp)
            return res1*res2
        else:
            res=exp(n//2)
            temp=res*res
            real_res.append(temp)
            return res*res
    else:
        real_res.append(2**n)
        return 2**n
fprimetwo=0
op=10**9+7
real_res=[]
exp(1000000000)
real_res=sorted(set(real_res))
exit(0)
for _ in range(int(input())):
    c,k=map(int,input().split())
    if k==0: continue #상수항 skip
    c*=k
    k-=1
    fprimetwo+=(c)*exp(k) if k>0 else c #1차 -> 상수항 처리
print(fprimetwo%(op))