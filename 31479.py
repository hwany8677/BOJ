#파싱 노가다
from sys import stdin
input=stdin.readline
def gcd(a,b):
    while(r>0):
        q=a//b; r=a%b 
        if r==0: break
        a,b=b,r
    return b
def derivative(info): #hmu if this is a bad practice
    for _ in range(2):
        if info[0]: 
            calcres_1=info[1]*info[4]
            calcres_2=info[2]%info[4]
            if calcres_2!=0:
                info[1]*=info[4]
            else: 
                info[2]//=info[4]
                info[0]=False
                info[3]=1
        else: info[3]*=info[4]
        info[4]-=1
    buf=""
    #Check exponent -> check coefficient
    if info[4]>0:
        if info[0]: buf+=f"{info[1]}/{info[2]}x" #Fractional
        elif info[3]==1: buf+="x" #coeff=1
        elif info[3]>1: buf+=f"{info[3]}x" #coeff>1
        if info[4]>1: buf+=f"^{info[4]}" #exp>1
    if info[4]==0: 
        if info[0]: buf+=f"{info[1]}/{info[2]}"
        else: buf+=f"{info[3]}"
        
    return buf
for _ in range(int(input())):
    i,m=input().split()
    i=i.strip("+Cx+D")
    #Parsing
    res=""; buf=""
    numer=0; denomi=0
    coeff=""
    is_fractional=False
    has_coeff=False
    #Reading i
    length=len(i)
    for idx in range(length):
        if i[idx]=="+" or i[idx]=="-" or idx==length-1: #Push buffer
            if coeff=="": coeff=0
            res=derivative([is_fractional,numer,denomi,coeff,exp])
            buf+=res+i[idx]
            #temp code
            print(res)
            res=""
            #real code do not remove
            is_fractional=False
            has_coeff=False
            numer=0; denomi=0
            coeff=""
            continue 
        if i[idx]=="/":
            numer=int(coeff)
            is_fractional=True
            coeff=""
            continue
        if i[idx]=="x":
            if not(has_coeff): coeff="1"
            if is_fractional: denomi=int(coeff)
            else: coeff=int(coeff)
            continue
        if i[idx]=="^": #No exponent lesser than ^2 can be found in this case 
            j=idx+1
            exp=""
            while (1): 
                if j==length or i[j]=='+' or i[j]=='-': break
                else: exp+=i[j]
                j+=1
            j-=1; idx=j; exp=int(exp)
            continue
        coeff+=i[idx]