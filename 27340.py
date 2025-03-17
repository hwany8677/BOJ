#A table always consists of 4 chairs
#Pitfall point: didn't say that every table color has to be unique
#n: number of tables
#m: number of chair colors
input=open(0).readline
n,m=map(int,input().split())
ai=list(map(int,input().split())) #len(ai)=m, determined
ai_verify=[False for _ in range(m)] #Couldn't come up with better idea :/
chairs_req=n*4
i,j=0,0
strike=0
while(chairs_req>0):
    if ai[i]>=4: 
        chairs_req-=4
        ai[i]-=4
        ai_verify[i]=True
    else: strike+=1
    i+=1
    if i==m: 
        if strike==m: break #Only triggers if chairs_req>0, does not interfere with other logics
        i=0
        strike=0
        j+=1
if strike==m: print("NE")
elif sum(ai_verify)<m: print("NE")
else: print("DA")
