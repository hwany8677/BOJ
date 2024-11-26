#A=10, B=11, ... , Z=35
#+9
#A=1, B=2, ..., Z=26
#ord(some character)-55
real_s=input()
s=''
res=''
for i in range(4,len(real_s)): s+=real_s[i]
for i in range(4): s+=real_s[i]
for char in s:
    if char.isalpha(): res+=str(ord(char)-55)
    else: res+=char
res=int(res)
print("correct" if res%97==1 else "incorrect")