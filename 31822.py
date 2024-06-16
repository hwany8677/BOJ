#Solving w/ what I know so far
retake=input()
match=[retake[i] for i in range(5)]
n=int(input())
count=0
for _ in range(n):
    buf=input()
    check=[buf[i] for i in range(5)]
    if match==check: count+=1
print(count)