target="UCPC"
s=input()
conquered=[False]*4 #U, C, P, C
for c in s:
    if c=='U': conquered[0]=True
    if c=='C': 
        if conquered[0]: conquered[1]=True
        else: continue
    if c=='P':
        if conquered[1]: conquered[2]=True
        else: continue
    if c=='C':
        if conquered[2]: conquered[3]=True
        else: continue
count=0
for bool in conquered: count+=1 if bool else 0
print("I love UCPC" if count==4 else "I hate UCPC")