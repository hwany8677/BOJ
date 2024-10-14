input=open(0).readline
buf=[]
bitmask=[0 for _ in range(26)]
for _ in range(int(input())):
    s=input().rstrip()
    bitmask[ord(s[0])-97]+=1
had_print=False
for i in range(26):
    if bitmask[i]>=5: 
        print(chr(i+97),end='')
        had_print=True
if not(had_print): print("PREDAJA")
else: print()
