input=open(0).readline
for _ in range(3):
    sigma=0
    for __ in range(int(input())): 
        n=int(input())
        sigma+=n
    print('+' if sigma>0 else 0 if sigma==0 else '-')