input=open(0).readline
h=int(input())
m=int(input())
for t in range(1,m+1):
    A=-6*(t**4)+h*(t**3)+2*(t**2)+t
    if A<=0: print(f"The balloon first touches ground at hour: {t}"); exit(0)
print("The balloon does not touch ground in the given time.")
