n,p=map(int,input().split())
record=[n]
i=0
while(1):
    n=list(str(n))
    res=0
    for digit in n: res+=int(digit)**p
    n=res
    if n in record: 
        print(record.index(n))
        break
    else: record.append(n)