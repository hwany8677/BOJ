"""
Total Σ of all citations articles published in the journal / 
Total articles published = ceil(Impact factor)
"""
#ALWAYS GETS ROUNDED
from math import ceil
a,i=input().split() 
a=int(a) #Articles published 
i=int(i) #Impact factor
sig=a*i
while(True):
    if ceil(sig/a)==i: sig-=1
    else:
        sig+=1
        break
print(sig)