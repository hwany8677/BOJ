input=open(0).readline
for _ in range(int(input())):
    s=input().rstrip()
    for i in range(len(s)-1,-1,-1): print(s[i],end='')
    print()
