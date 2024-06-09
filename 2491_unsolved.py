n=int(input())
buf=list(map(int,input().split()))
if n==1: print(1)
else:
    count,mx=1,1
    for i in range(0,len(buf)-1):
        if i==0:
            prevNext=0 if buf[i]<buf[i+1] else 1 if buf[i]>buf[i+1] else 2
            count+=1 
            continue
        if buf[i]==buf[i+1]: 
            prevNext=2
            count+=1
        elif buf[i]<buf[i+1]:
            if prevNext==2: prevNext=0
            if not(prevNext): count+=1
            else:
                mx=count if count>=mx else mx
                prevNext=0
                count=2
        elif buf[i]>buf[i+1]:
            if prevNext==2: prevNext=1
            if prevNext: count+=1
            else:
                mx=count if count>=mx else mx
                prevNext=1
                count=2
    print(mx if mx>=count else count)