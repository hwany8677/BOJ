input=open(0).readline
for i in range(int(input())):
    numbers=[0 for _ in range(10)]
    real_n=int(input())
    n=real_n
    to_cont=False
    while(n!=0):
        str_n=str(n)
        for char in str_n: numbers[int(char)]=1
        if sum(numbers)==10: 
            print(f"Case #{i+1}: {n}")
            to_cont=True
            break
        n+=real_n
    if to_cont: continue
    else: print(f"Case #{i+1}: INSOMNIA")
