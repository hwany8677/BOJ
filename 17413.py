s=input()
buf=[]
inside_bracket=False
temp=''
for char in s:
    if char==' ' and not(inside_bracket):
        buf.append(temp)
        temp=''
    elif char=='<': 
        buf.append(temp)
        temp='<'
        inside_bracket=True
    elif char=='>':
        temp+='>'
        buf.append(temp)
        inside_bracket=False
        temp=''
    else: temp+=char
buf.append(temp)
for j in range(len(buf)-1):
    if buf[j]=='': continue
    if buf[j][0]=='<': print(buf[j],end='')
    else: 
        for i in range(len(buf[j])-1,-1,-1): print(buf[j][i],end='')
        if buf[j+1][0]!='<': print(' ',end='')
try: 
    for i in range(len(buf[j+1])-1,-1,-1): print(buf[j+1][i],end='')
except NameError: 
    for i in range(len(s)-1,-1,-1): print(s[i],end='')
print()