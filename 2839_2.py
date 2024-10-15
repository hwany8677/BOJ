#괴씸죄로 날먹할께요
n=int(input())
count=0
if n%5==0: print(n//5)
elif n//10==0:
    if n%3==0: print(n//3)
    elif n%5==0: print(n//5)
    elif n==8: print(2)
    else: print(-1)
else:
    count=0
    while(n>0):
        n-=3
        count+=1
        if n%5==0:
            count+=n//5
            print(count)
            exit(0)
    print(-1)
