#Naive approach
time=[0 for _ in range(1000000)]
n=int(input())
for _ in range(n):
    s,e=map(int,input().split())
    for i in range(s-1,e):
        time[i]+=1
q=int(input())
want_to_know=list(map(int,input().split()))
for element in want_to_know: print(time[element-1])