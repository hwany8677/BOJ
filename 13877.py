input=open(0).readline
p=int(input())
for i in range(p): 
    k,buf=input().rstrip().split()
    length=len(buf)
    print(k,end=' ')
    #Octal
    res=0
    for j in range(length):
        current=int(buf[j])
        if current<8: res+=current*(8**(length-1-j))
        else:
            res=0
            break
    print(res,end=' ')
    #Decimal
    print(buf,end=' ')
    #Hexadecimal
    res=0
    for j in range(length):
        current=int(buf[j])
        res+=current*(16**(length-1-j))
    print(res)
