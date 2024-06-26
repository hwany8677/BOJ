for i in range(int(input())):
    a,b=map(int,input().split())
    count=0
    c=1
    while(1):
        if c**3<a: c+=1
        elif c**3>b: break
        else: 
            c+=1
            count+=1
    print("Case #{}: {}".format(i+1, count))