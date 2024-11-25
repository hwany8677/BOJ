input=open(0).readline;combo={1:"",2:"double",3:"triple",4:"quadruple",5:"quintuple",6:"sextuple",7:"septuple",8:"octuple",9:"nonuple",10:"decuple"};number={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
for case in range(int(input())):
    buf=input().rstrip().split();output_buf=[];phone=buf[0];method=list(map(int,buf[1].split('-')));i=0;output_i=-1
    for cap in method:
        j=1;prev=phone[i+0];output_buf.append([1,prev]);output_i+=1
        while(j<cap):
            current=phone[i+j]
            if prev==current: output_buf[output_i][0]+=1
            else:output_buf.append([1,current]);output_i+=1
            prev=phone[i+j];j+=1
        i+=j
    print(f"Case #{case+1}:",end=' ')
    for buf in output_buf:
        if buf[0]>10: print(f"{number[buf[1]]} "*buf[0],end='')
        elif buf[0]>1: print(combo[buf[0]],number[buf[1]],end=' ')
        else: print(number[buf[1]],end=' ')
    print()
