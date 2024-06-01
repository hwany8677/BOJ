#Filthy code
#귀찮아서 1066바이트의 광기짓을 해봤어요
t=int(input())
for _ in range(t):
    k=int(input())
    n=int(input())
    floor0=[i for i in range(15)]
    res=list(floor0)
    if k==0: print(floor0[n])
    else: 
        for i in range(k): res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8],res[9], res[10],res[11],res[12],res[13],res[14]=res[1],res[1]+res[2],res[1]+res[2]+res[3],res[1]+res[2]+res[3]+res[4],res[1]+res[2]+res[3]+res[4]+res[5],res[1]+res[2]+res[3]+res[4]+res[5]+res[6],res[1]+res[2]+res[3]+res[4]+res[5]+res[6]+res[7],res[1]+res[2]+res[3]+res[4]+res[5]+res[6]+res[7]+res[8],res[1]+res[2]+res[3]+res[4]+res[5]+res[6]+res[7]+res[8]+res[9],res[1]+res[2]+res[3]+res[4]+res[5]+res[6]+res[7]+res[8]+res[9]+res[10],res[1]+res[2]+res[3]+res[4]+res[5]+res[6]+res[7]+res[8]+res[9]+res[10]+res[11],res[1]+res[2]+res[3]+res[4]+res[5]+res[6]+res[7]+res[8]+res[9]+res[10]+res[11]+res[12],res[1]+res[2]+res[3]+res[4]+res[5]+res[6]+res[7]+res[8]+res[9]+res[10]+res[11]+res[12]+res[13],res[1]+res[2]+res[3]+res[4]+res[5]+res[6]+res[7]+res[8]+res[9]+res[10]+res[11]+res[12]+res[13]+res[14]
    print(res[n])