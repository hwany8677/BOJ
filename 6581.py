from sys import stdin
buf=stdin.readline()
s=''+buf
while (1):
    buf=stdin.readline()
    if buf=='': break
    s+=buf
s.split()
chars=0
for i in range(0,len(s)):
    if s[i]=='<br>':
        print()
        chars=0
    elif s[i]=='<hr>':
        print('-'*80)
        chars=0
    else:
        if chars+len(s[i])>80:
            chars=len(s[i])
            print(f"\n{s[i]} ",end='')