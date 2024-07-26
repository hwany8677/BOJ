s=input()
conv_count=0
n=int(s) if len(s)==1 else 0
length=len(s)
while(length>1):
    conv_count+=1
    n=0
    for num in s: n+=int(num)
    s=str(n)
    length=len(s)
if n%3==0:
    print(conv_count)
    print("YES")
else:
    print(conv_count)
    print("NO")