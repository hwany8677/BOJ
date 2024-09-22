alpha_c=[0 for _ in range(26)]
s=input()
for alpha in s:
    temp=ord(alpha)
    if temp>96: alpha_c[temp-97]+=1
    else: alpha_c[temp-65]+=1
mx=max(alpha_c); loc=0
has_mx=False
for i in range(26):
    if mx==alpha_c[i]: 
        if has_mx: print("?"); exit(0)
        has_mx=True
        loc=i
print(chr(loc+65))