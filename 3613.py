s=input()
#'_asdf', 'asdf_', 'Asdf'
if s[0]=='_' or ord(s[0])<97 or s[len(s)-1]=='_': print("Error!"); exit(0)
copy_s=s.split('_')
if len(copy_s)>1: #It's C++.
    for i in range(len(copy_s)):
        #'asdf__asdf'
        if copy_s[i]=='': print("Error!"); exit(0)
    #'asdfAsdf_asdf'
    for i in range(len(copy_s)):
        for j in range(len(copy_s[i])):
            if ord(copy_s[i][j])<97 and copy_s[i][j]!='_': print("Error!"); exit(0)
    print(copy_s[0],end='')
    for i in range(1,len(copy_s)):
        for j in range(len(copy_s[i])):
            if j==0: print(chr(ord(copy_s[i][j])-32),end='')
            else: print(copy_s[i][j],end='')
else: #It's Java.
    for char in s:
        if ord(char)<97: print('_'+chr(ord(char)+32),end='')
        else: print(char,end='')