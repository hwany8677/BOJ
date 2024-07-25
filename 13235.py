s=input()
for i in range(int(len(s)/2)):
    if s[i]!=s[len(s)-1-i]:  
        print("false")
        exit(0)
print("true")
