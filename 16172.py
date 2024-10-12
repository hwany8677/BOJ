#나는 친구가 적다 (x)
#나는 친구가 (Large하게) 적다 (o)
#2%, 4%, 11% WA
s=input()
to_find=input()
length=len(to_find)
s_convert=''
for char in s:
    if char.isalpha(): s_convert+=char
s=s_convert
if len(s)==0:
    print(0)
    exit(0)
if to_find in s: print(1)
else: print(0)