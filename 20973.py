alpha=input()
s=input()
i=0
count=0
while(i<len(s)):
    target=s[i]
    for char in alpha:
        if char==target: 
            i+=1
            if i>len(s)-1: break
            target=s[i]
    count+=1
print(count)