#ord('!')=33 -> 0
#LUMI = 43*(69^3)+52*(69^2)+44*(69^1)+40*(69^0)
from math import ceil
def toBase10(base,number):
    length=len(number)
    base10=0
    for i in range(length):
        base10+=(ord(number[i])-33)*(base**(length-1-i))
    return base10
n=int(input())
a=list(input())
b=list(input())
AisNegative=True if a[0]=='~' else False
BisNegative=True if b[0]=='~' else False
if AisNegative: a.remove('~')
if BisNegative: b.remove('~')
a_length=len(a)
b_length=len(b)
a_base10=toBase10(n,a)
b_base10=toBase10(n,b)
res=a_base10*b_base10 #10진수
res_baseN=[] #1번째 자리, 2번째 자리, ... -> 나중에 뒤집음
q=res//n 
r=res%n
while(1):
    if r==0: break
    res_baseN.append(abs(r))
    r=q%n
    q=q//n if n>0 else ceil(q/n)
res_baseN.reverse()
for number in res_baseN:
    print(chr(number+33),end='')
print()