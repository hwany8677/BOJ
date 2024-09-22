from sys import stdin
input=stdin.readline

for _ in range(int(input())):
    a,b=map(float,input().split())
    h=(2*a)/b
    print("The height of the triangle is {:.2f} units".format(h))