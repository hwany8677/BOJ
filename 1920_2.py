#Naive method - does not work
n=int(input())
lisT=list(map(int,input().split()))
n_find=int(input())
to_find=list(map(int,input().split()))
for num in to_find:
    if num in lisT: print(1)
    else: print(0)