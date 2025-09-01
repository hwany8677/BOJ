#'.And'면 다른문장, 'Man.'이면 같은문장???
#:blobdizzy:
input=open(0).readline
n=int(input())
s=input().rstrip()
if n<=25:
    print(s)
    exit(0)
begin,end=11,n-12
#print(*s[begin:end+1],'\n',end='')
scope=s[begin:end+1]
scope_res=scope.find('.')
if scope_res==end-begin or scope_res==-1:
    i=0
    while(i<n):
        if i>=begin and i<=end:
            print("...",end='')
            i+=end-begin+1
        else:
            print(s[i],end='')
            i+=1
else:
    begin,end=9,n-11
    i=0
    while(i<n):
        if i>=begin and i<=end:
            print("......",end='')
            i+=end-begin+1
        else:
            print(s[i],end='')
            i+=1
print()
