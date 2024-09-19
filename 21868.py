#하 시발
#절댓값 하나때문에 내 오후를 날렸어
#미적못하는바부

#delta=epsilon/coefficient
#abs(a*(x-x0))<epsilon
#therefore epsilon/a=delta
# def gcd(a,b):
#     while(r>0):
#         q=a//b; r=a%b 
#         if r==0: break
#         a,b=b,r
#    return b
ep_numer,ep_denomi=map(int,input().split())
s=list(map(int,input().split()))
x=s[0]
const=s[1] 
x0=int(input())
L=x*x0+const
print(L) 
ep_denomi*=abs(x)
if abs(x)<1: print(0,0)
# 필요없는 코드
# elif ep_denomi>10**8: 
#     # if ep_numer>ep_denomi: to_divide=gcd(ep_numer,ep_denomi)
#     # else: to_divide=gcd(ep_denomi,ep_numer)
#     # ep_numer//=to_divide
#     # ep_denomi//=to_divide
#     if ep_numer==1: print(0,0)
#     else:
#         if ep_numer%2==0 and ep_denomi%2==0: print(ep_numer//2,ep_denomi//2)
#         elif ep_denomi%ep_numer: print(0,0)
else: print(ep_numer,ep_denomi)