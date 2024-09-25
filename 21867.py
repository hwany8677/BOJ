n=int(input())
s=input()
_=1
for char in s:
    if char=='J' or char=='A' or char=='V': continue
    else: print(char,end=''); _=0
if _: print("nojava")