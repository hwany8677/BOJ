import re
input=open(0).readline
tool=re.compile(r"[A-Za-z\-]")
i=0
mx,mx_str=0,""
while(1):
    buf=input().rstrip().split()
    print(buf)
    for string in buf:
        res=tool.findall(string)
        print(res)
        input()
        w_length=len(res) if len(string)==len(res) else len(string)-(len(string)-len(res))
        if w_length>mx:
            mx=w_length
            mx_str=string
    if len(buf)!=0:
        if buf[len(buf)-1]=="E-N-D": break
    i+=1
print(mx_str.lower())
