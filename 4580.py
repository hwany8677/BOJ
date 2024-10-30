input=open(0).readline
buf=list(map(int,input().split()))
amount=0
while(len(buf)>1 and buf[0]!=0):
    n=buf.pop(0)
    prev=buf[0]
    amount=prev
    print("1 "*prev,end='')
    for i in range(1,n):
        element=buf[i]
        amount=element-prev
        print(f"{i+1} "*amount,end='')
        prev=element
    print()
    buf=list(map(int,input().split()))