s=input()
s_number=int(s)
conv_count=0
while(len(s)>1):
    conv_count+=1
    s_number=0
    for num in s: s_number+=int(num)
    s=str(s_number)
if s_number%3==0:
    print(conv_count)
    print("YES")
else:
    print(conv_count)
    print("NO")