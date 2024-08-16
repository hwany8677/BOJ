pre_defined=["1", "1 2", "1 2 1 2"]
n=int(input())
if n<5: print(pre_defined[n-2])
else:
    for i in range(1,n+1):
        if i==n: print("3" if i%2 else "2")
        elif i%2: print("1 ",end='')
        else: print("2 ",end='')