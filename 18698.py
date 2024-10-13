input=open(0).readline
for _ in range(int(input())):
    s=input().rstrip()
    count=0
    for char in s:
        if char=='D': break
        else: count+=1
    print(count)