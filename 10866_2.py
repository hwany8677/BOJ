#There was an attempt...
from sys import stdin
i=stdin.readline;p=print;d=[0 for _ in range(20000)];f=10001;b=9999
for _ in range(int(i())):
    s=i().rstrip().split()
    if len(s)==2: c,x=s[0],int(s[1])
    else: c=s[0]
    if c=="push_front":
        d[f-1]=x
        #In case of deque contains nothing
        if f>b:f-=1;b+=1
        else: f-=1
    if c=="push_back":
        d[b+1]=x
        if f>b:f-=1;b+=1
        else: b+=1
    if c=="pop_front":
        if f>b:p(-1)
        else:
            p(d[f]);d[f]=0
            if f==b:f+=1;b-=1
            else:f+=1
    if c=="pop_back":
        if f>b:p(-1)
        else: 
            p(d[b]);d[b]=0
            if f==b:f+=1;b-=1
            else:b-=1
    if c=="size":p(0 if f>b else b-f+1)
    if c=="empty":p(1 if f>b else 0)
    if c=="front":p(-1 if f>b else d[f])
    if c=="back":p(-1 if f>b else d[b])