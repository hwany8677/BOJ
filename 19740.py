input=open(0).readline
mn=0
for _ in range(int(input())):
    s=input().rstrip()
    int_s=int(s)
    length=len(s)
    if mn==0: mn=10**(length-1)
    if int_s>mn: mn=int_s
print(mn)
print(10**(length)-1)