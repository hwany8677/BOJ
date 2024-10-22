#Including the gen
input=open(0).readline
t=[]
w=[0]
sigma=0
for i in range(1,302):
    sigma=sum([j for j in range(1,i+1)])
    t.append(sigma)
sigma=0
for i in range(1,301):
    sigma+=i*t[i]
    w.append(sigma)
for _ in range(int(input())): print(w[int(input())])
