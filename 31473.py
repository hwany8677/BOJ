#sigA>sigB or sigA<sigB
def gcd(a,b):
    q=a//b
    r=a%b
    while(r>0): 
        a,b=b,r
        q,r=a//b,a%r
    return b
n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
sigA=sum(A)
sigB=sum(B)
sig_gcd=gcd(sigA,sigB)
mn_a,mn_b=sigB//sig_gcd,sigA//sig_gcd
print(mn_a,mn_b)
