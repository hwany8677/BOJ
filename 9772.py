from sys import stdin
input=stdin.readline
a,b=map(float,input().split())
while(not(a==0 and b==0)):
    if a>0 and b>0: print("Q1")
    elif a<0 and b>0: print("Q2")
    elif a<0 and b<0: print("Q3")
    elif a>0 and b<0: print("Q4")
    else: print("AXIS")
    a,b=map(float,input().split())
print("AXIS")