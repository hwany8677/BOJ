#나는 친구가 적다 (x)
#나는 친구가 (Large하게) 적다 (o)
#2%, 4%, 11% WA
s=input()
to_find=input()
length=len(to_find)
chain=0
i=0
for char in s:
    if i>length-1: break
    # print(char,to_find[i],chain)
    if char==to_find[i]:
        chain+=1
        i+=1
    elif char!=to_find[i]:
        if char.isalpha():
            if char==to_find[0]:
                chain=1
                i=1
            else:
                chain=0
                i=0
print(1 if chain==length else 0)
