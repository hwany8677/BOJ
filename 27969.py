#대괄호 열때마다 +8byte
#정수일때 마다 +8byte
#문자열일때 마다 +( len(s[i])+12 )byte
#0~9는 아스키 48~57
#A부터 아스키 65
s=input().split()
sigma=0
for element in s:
    if element=='[': sigma+=8
    temp=ord(element[0])
    if temp>47 and temp<58: sigma+=8
    if (temp>64 and temp<91) or temp>96:
        sigma+=len(element)
        sigma+=12
print(sigma)