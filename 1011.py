#산만함 MAX
#1~46342까지의 모든 경우를 따진다
#46341^2, 46341*46342
input=open(0).readline
buf=[i**2 for i in range(1,46343)]
buf2=[i*(i+1) for i in range(1,46344)]
buf.sort()
buf2.sort()
for _ in range(int(input())):
    x,y=map(int,input().split())
    dist=y-x
    #dist>final[i] 인 경우 바로 멈춤
    i=0
    res=0
    while(1):
        if buf[i]<dist and dist<buf2[i]:
            print("broke",i,f"dist={dist}",f"final[i]={final[i]}")
            i+=1
            res=i+1
            break
        if buf2[i]<dist and dist<buf[i+1]:
            print("broke",i,f"dist={dist}",f"final[i]={final[i]}")
            
            break
        i+=1
    print()
