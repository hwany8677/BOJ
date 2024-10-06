n=int(input())
if (n==1):
    input()
    print(0)
    exit(0)
buf=list(map(int,input().split()))
mn,ai_aj=buf[0],0
print(0,end=' ')
for i in range(1,n):
    if buf[i]<=mn: 
        print(ai_aj, end=' ')
        mn=buf[i]
    elif buf[i]>mn:
        temp=buf[i]-mn
        if temp<ai_aj:
            print(ai_aj,end=' ')
            continue
        else: 
            ai_aj=temp
            print(ai_aj,end=' ')