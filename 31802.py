#0에서 1, 1에서 2, 2에서 3, ..., i-1에서 i <<< p개
def Sn(lisT): 
    S=[lisT[0]]
    for i in range(1,len(lisT)):
        S.append(lisT[i]+S[i-1])
    return S
p=int(input())
def_integral=list(map(int,input().split()))
a,b=map(int,input().split())
if a==b: print(0)
else:
    def_Sn=Sn(def_integral)