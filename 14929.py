#Alt method: don't create x_sum as list, run for loop with 'i' decreasing
n=int(input())
x=list(map(int,input().split()))
x_sum=[x[0]] 
for i in range(1,n):
    x_sum.append(x[i]+x_sum[i-1])
sigma=0
for i in range(n):
    sigma+=x[i]*(x_sum[n-1]-x_sum[i])
print(sigma)