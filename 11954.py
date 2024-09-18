#Filthy code
#tf is this code
s=input().split(',')
indent=0
if s[0]=="{}": print("{\n}"); exit(0)
if len(s)==1:
    print("{\n  ",end='')
    for char in s[0]:
        if char=='{' or char=='}': continue
        print(char,end='')
    print("\n}")
    exit(0)
for i in range(len(s)):
    if s[i]=="{}}":
        print(" "*indent+"{")
        print(" "*indent+"}")
        print("}")
        continue
    if s[i]=="{}": 
        print("{\n},")
        continue
    if s[i][0]=='{':
        print(" "*indent+'{')
        indent+=2
        print(" "*indent+s[i][1:],end='')
        print(',')
        continue
    if s[i][len(s[i])-1]=='}':
        print(" "*indent,end='')
        for j in range(len(s[i])-1): print(s[i][j],end='')
        print()
        indent-=2
        print(" "*indent+'}',end='')
        if i<len(s)-1: print(",")
        else: print()
        continue
    print(" "*indent+s[i]+',')