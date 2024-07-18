for _ in range(int(input())):
    buf=input().split()
    R,C=int(buf[0]),int(buf[1])
    mtrx=[]
    i=0
    buf=buf[2]
    while(i<len(buf)):
        mtrx.append(buf[i:i+C])
        i+=C
    