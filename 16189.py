s=input()
k=int(input())
length=len(s)
for i in range(int(length/2)):
    if s[i]!=s[length-1-i]:
        print("NO")
        exit(0)
print("YES")