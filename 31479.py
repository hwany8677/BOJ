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
def derivative(info): #hmu if this is a bad practice << it is, past me :/
    is_fractional,numer,denomi,coeff,exp=info[0],info[1],info[2],info[3],info[4]
    for _ in range(2):
        if is_fractional: 
            # calcres_1=info[1]*info[4]
            # calcres_2=info[2]%info[4]
            # if calcres_2!=0:
            #     info[1]*=info[4]
            # else: 
            #     info[2]//=info[4]
            #     if info[2]==1: #분모가 1이 될 경우 
            #         info[0]=False
            #         info[3]=1
            numer*=exp
        elif coeff=='1': coeff=1; coeff*=coeff
        else: coeff*=exp
        exp-=1 #<< this POS is the culprit
    rt_buf=""
    #Check if fraction is improper fraction & check if its divisibility
    if is_fractional:
        #가분수인지 진분수인지 채크
        if numer>denomi:
            num_denom_gcd=gcd(numer,denomi)
            numer//=num_denom_gcd
            denomi//=num_denom_gcd
            if denomi==1: #분모가 1이 되었으므로 정수
                is_fractional=False
                coeff=numer
        elif numer<denomi:
            num_denom_gcd=gcd(denomi,numer)
            numer//=num_denom_gcd
            denomi//=num_denom_gcd
        else: #2/2, 4/4와 같은 경우
            is_fractional=False
            coeff=1
    #Check exponent -> check coefficient
    if exp>0:
        print(coeff)
        if is_fractional: rt_buf+=f"{numer}/{denomi}x" #Fractional
        elif coeff==1: rt_buf+="x"
        elif coeff>1: rt_buf+=f"{coeff}x"
        if info[4]>1: rt_buf+=f"^{exp}"
    if exp==0: 
        if is_fractional: rt_buf+=f"{numer}/{denomi}"
        else: rt_buf+=f"{coeff}"
        
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
            #below is real code do not remove
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