#안되는코드
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
start=0
end=length-1
while(end<len(s)):
    count=0
    for i in range(start,end+1):
        if s[i]==to_find[i-start]: count+=1
    if count==length: break
    start+=1
    end+=1
print(1 if count==length else 0)