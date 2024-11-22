s=input()
for i in range(len(s)):
    char=s[i]
    if char=='d' or char=='D':
        if i<len(s)-1:
            if s[i+1]=='2': print("D2"); exit(0)
print("unrated")