n=int(input())
sigma=0
for i in range(n+1):
    for j in range(i+1):
        sigma+=i+j
print(sigma)