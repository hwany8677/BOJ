from sys import stdin
input=stdin.readline

while(1):
    n=float(input())
    if n==-1: break
    print("Objects weighing {:.2f} on Earth will weigh".format(n), "{:.2f}".format(n*0.167), "on the moon.")