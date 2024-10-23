input=open(0).readline
buf=input()
while(buf!=''):
    n,s=map(int,buf.split())
    n+=1
    print(s//n)
    buf=input()
