from math import floor
while(True):
    s=input()
    if s=="0": break
    c=0
    for i in range(0,floor(len(s)/2)):
        if s[i]==s[len(s)-1-i]: c+=1
    print("yes" if c==floor(len(s)/2) or len(s)==1 else "no")