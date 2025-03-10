#Leading zeros - careful!
input=open(0).readline
inde_num=[]
for _ in range(int(input())):
    buf=input().rstrip()
    i=0
    num_to_create=''
    while(i<len(buf)):
        if buf[i].isalpha(): 
            if len(num_to_create)==0: i+=1
            else:
                inde_num.append(int(num_to_create))
                num_to_create=''
                i+=1
        else: 
            num_to_create+=buf[i]
            i+=1
    if len(num_to_create)>0: inde_num.append(int(num_to_create))
inde_num.sort()
for num in inde_num: print(num)
