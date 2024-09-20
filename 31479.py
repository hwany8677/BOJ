#파싱 노가다
############## 생각 포인트 ##############
# 1. 적분상수로 이루어진 다항식 Cx+D는
#    항상 따라붙는다.
# 2. 1번 외 다항식은 전부 2제곱 이상이다.
#    이때 상수항이 생기는 일은 해당 항이
#    **2제곱** 일 때 ***만*** 이다.
############## 생각 포인트 ############## 
from sys import stdin
input=stdin.readline
def gcd(a,b):
    q=a//b; r=a%b 
    while(r>0):
        if r==0: break
        a,b=b,r
        q=a//b; r=a%b 
    return b
def derivative(info): #hmu if this is a bad practice
    for _ in range(2):
        if info[0]: 
            # calcres_1=info[1]*info[4]
            # calcres_2=info[2]%info[4]
            # if calcres_2!=0:
            #     info[1]*=info[4]
            # else: 
            #     info[2]//=info[4]
            #     if info[2]==1: #분모가 1이 될 경우 
            #         info[0]=False
            #         info[3]=1
            info[1]*=info[4]
        elif info[3]=='1': info[3]=1; info[3]*=info[3]
        else: info[3]*=info[4]
        info[4]-=1
    rt_buf=""
    #Check if fraction is improper fraction & check if its divisibility
    if info[0]:
        #가분수인지 진분수인지 채크
        if info[1]>info[2]:
            num_denom_gcd=gcd(info[1],info[2])
            info[1]//=num_denom_gcd
            info[2]//=num_denom_gcd
            if info[2]==1: #분모가 1이 되었으므로 정수
                info[0]=False
                info[3]=info[1]
        elif info[1]<info[2]:
            num_denom_gcd=gcd(info[2],info[1])
            info[1]//=num_denom_gcd
            info[2]//=num_denom_gcd
        else: #2/2, 4/4와 같은 경우
            info[0]=False
            info[3]=1
    #Check exponent -> check coefficient
    if info[4]>0:
        if info[0]: rt_buf+=f"{info[1]}/{info[2]}x" #Fractional
        elif info[3]==1: rt_buf+="x" #coeff=1
        elif info[3]>1: rt_buf+=f"{info[3]}x" #coeff>1
        if info[4]>1: rt_buf+=f"^{info[4]}" #exp>1
    if info[4]==0: 
        if info[0]: rt_buf+=f"{info[1]}/{info[2]}"
        else: rt_buf+=f"{info[3]}"
        
    return rt_buf
for _ in range(int(input())):
    i,m=input().split()
    # i=i.strip("+Cx+D") #<---안됨
    temp=''
    for k in range(len(i)-5): temp+=i[k]
    i=temp
    #### PARSING START ####
    res=""; buf=""
    numer=0; denomi=0
    coeff=""; exp=""
    is_fractional=False; exp_decided=False
    #Reading i
    length=len(i)
    for idx in range(length):
        if i[idx]=="+" or i[idx]=="-" or idx==length-1: #Push buffer
            if coeff=="": coeff=0
            buf=derivative([is_fractional,numer,denomi,coeff,exp])
            res+=buf
            if idx<length-1: res+=i[idx]
            #temp code
            # print(buf)
            # buf=""
            #real code do not remove
            numer=0; denomi=0
            coeff=""; exp=""
            is_fractional=False; exp_decided=False
            continue 
        if i[idx]=="/":
            numer=int(coeff)
            is_fractional=True
            coeff=""
            continue
        if i[idx]=="x":
            if is_fractional: denomi=int(coeff)
            elif coeff=='': coeff='1'
            # else: coeff=int(coeff)
            continue
        if i[idx]=="^": #No exponent lesser than ^2 can be found in this case 
            j=idx+1
            while(1): 
                if j==length or i[j]=='+' or i[j]=='-': break
                else: exp+=i[j]
                j+=1
            j-=1; idx=j; exp=int(exp)
            exp_decided=True
            continue
        if not(exp_decided): coeff+=i[idx]
    #### PARSING END ####
    if res==m: print("Yes")
    else: print("No")