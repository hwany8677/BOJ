a=int(input())
b=int(input())
if a%3!=b%3:
    print(-1)
    exit(0)
wa,wb=a//3,b//3
print(wa,a%3,wb)
