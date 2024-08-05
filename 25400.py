n=int(input())
buf=list(map(int,input().split()))
expected=1
c=0
for num in buf:
    if num!=expected:
        c+=1
    elif num==expected:
        expected+=1
print(c)