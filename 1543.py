s=input()
search=input()
to_search=0
match=0
i=0
while(i<len(s)):
    char=s[i]
    if char==search[to_search]: to_search+=1
    else: 
        to_search=0
        continue
    if to_search==len(search): 
        match+=1
        to_search=0
    i+=1
print(match)

