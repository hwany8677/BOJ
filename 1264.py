#딕셔너리 쓸 줄 모름
while(True):
    c=0
    s=input()
    if s[0]=='#': break
    for i in s:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            c+=1
    print(c)