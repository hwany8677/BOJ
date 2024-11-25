def M(s):
    s=s.split('+')
    res=0
    hasStar=False
    for lisT in s: 
        if '*' in lisT: hasStar=True
    if not(hasStar):
        for element in s: res+=int(element)
        return res
    else: #섞인 경우
        for element in s:
            if '*' in element:
                temp=1
                element=list(map(int,element.split('*')))
                for num in element: temp*=num
                res+=temp
            else: res+=int(element)
    return res
def L(s):
    res=int(s[0])
    i=0
    while(i<len(s)-2):
        if s[i+1]=='+': res+=int(s[i+2])
        elif s[i+1]=='*': res*=int(s[i+2])
        i+=2
    return res
s=input().rstrip()
n=int(input())
res=[0,0]
res[0]=1 if M(s)==n else 0
res[1]=1 if L(s)==n else 0
if sum(res)==0: print('I')
elif sum(res)==2: print('U')
elif res[0]: print('M')
elif res[1]: print('L')