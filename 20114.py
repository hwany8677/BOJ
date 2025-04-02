#h x w 범위 내에
#1. '?'만 있지 않아야 하고
#2. 문자가 단 하나만 있어야 한다.
n,h,w=map(int,input().split())
buf=[]
for _ in range(h): buf.append(input())
res=''
k=0
while(k<n):
    only_qmark=True
    char=''
    for i in range(h):
        for j in range(k*w,(k+1)*w):
            current=buf[i][j]
            if current.isalpha():
                char=current
                only_qmark=False
    if only_qmark: res+='?'
    else: res+=char
    k+=1
print(res)
