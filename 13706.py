#Babylonian method (with rounding)
n=int(input())
a=len(str(n))*(10**(len(str(n))//2-1))
while(1):
    b=(a+n//a)//2
    if a==b: break
    a=b
print(int(a))