n=int(input())
c=1
while(n!=0):
    pizza=[]
    for _ in range(n):
        d,p=map(int,input().split())
        d2=d/2
        pizza.append((d,d2*d2*3/p))
    pizza.sort(key=lambda x:x[1])
    print(f"Menu {c}: {pizza[n-1][0]}")
    n=int(input())
    c+=1