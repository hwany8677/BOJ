#& -> max, | -> min
#'&' first, '|' comes last
input=open(0).readline
for _ in range(int(input())):
    s=input().rstrip().split(',')
    i=0
    while(i<len(s)): 
        s[i]=s[i].split(':')
        i+=1
    cond=input().rstrip().split('|')
    i=0
    while(i<len(cond)):
        cond[i]=cond[i].split('&')
        i+=1
    res=[]
    for ampersand in cond:
        mx=0
        for element in ampersand:
            i=0
            while(s[i][0]!=element): i+=1
            val=int(s[i][1])
            if val>mx: mx=val
        res.append(mx)
    print(min(res))