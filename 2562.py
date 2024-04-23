mx,max=0,0
for i in range(0,9):
    n=int(input())
    if n>=max:
        max=n
        mx=i+1
print(max)
print(mx)