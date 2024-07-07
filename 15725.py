#일차 일변수 다항식 -> ax+b꼴
s=input()
if 'x' in s: #6x -6x 6x+6 -6x+6
    s=s.split('x')
    if s[0]=='-': print(-1)
    elif s[0]=='': print(1)
    elif s[0]=='0': print(0)
    else: print(s[0])
else: print(0)