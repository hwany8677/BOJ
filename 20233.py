#기본, 초과, 기본, 초과
a=int(input()); x=int(input())
b=int(input()); y=int(input())
t=int(input())
res1,res2=a,b
if t>30: res1+=(t-30)*x*21
if t>45: res2+=(t-45)*y*21
print(res1,res2)
