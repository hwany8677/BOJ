input=open(0).readline
s=input().rstrip()
while(s!='#'):
    for i in range(len(s)-1):
        char=s[i]
        if not(char.isalpha()): print(char,end='')
        else:
            conv_char=ord(char)+5
            
            print(chr(conv_char),end='')
    print()
    s=input().rstrip()