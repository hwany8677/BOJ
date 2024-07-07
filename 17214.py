#일차항의 계수(x)는 무조건 2의 배수로 주어짐
s=input()
if 'x' in s:
    s=s.split('x')
    coeff_1=int(int(s[0])/2)
    if s[1]=='': 
        if coeff_1==1: print("xx+W")
        elif coeff_1==-1: print("-xx+W")
        else: print(f"{coeff_1}xx+W")
    else: 
        coeff_0=int(s[1])
        if coeff_1==1: print("xx",end='')
        elif coeff_1==-1: print("-xx",end='')
        else: print(f"{coeff_1}xx",end='')
        
        if coeff_0==1: print("+x+W")
        elif coeff_0==-1: print("-x+W")
        else: print("+" if coeff_0>0 else "",f"{coeff_0}x+W",sep='')
else: 
    if s=='-1': print("-x+W")
    elif s=='1': print("x+W")
    else: print(f"{s}x+W" if s!='0' else "W")