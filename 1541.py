#브루포스 느낌남
s=input()
if '-' not in s: #덧셈만 있는경우
    s=s.split('+')
    sigma=0
    for num in s: sigma+=int(num)
    print(sigma)
    exit(0)
elif '+' not in s: #뺄셈만 있는경우
    s=s.split('-')
    sigma=int(s[0])*2
    for num in s: sigma-=int(num)
    print(sigma)
    exit(0)
else:
    sigma=0
    to_calc=''
    mode=0 #0: 덧셈, 1: 뺄셈
    for i in range(len(s)):
        if s[i].isnumeric():
            to_calc+=s[i]
        else:
            sigma=int(to_calc)
            to_calc=''
            if s[i]=='-': mode=1
            break
    for j in range(i+1,len(s)):
        if s[j].isnumeric():
            to_calc+=s[j]
        else:
            sigma=sigma+int(to_calc) if mode==0 else sigma-int(to_calc)
            to_calc=''
        if s[j]=='-': mode=1
sigma-=int(to_calc)
print(sigma)