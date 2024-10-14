s=input()
zero_part=0
one_part=0
prev=s[0]
for i in range(1,len(s)):
    digit=s[i]
    if digit!=prev:
        if digit=='0': one_part+=1
        elif digit=='1': zero_part+=1
        prev=s[i]
if prev=='0': zero_part+=1
elif prev=='1': one_part+=1
if one_part==zero_part: print(zero_part)
elif one_part>zero_part: print(zero_part)
else: print(one_part)
