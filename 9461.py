from sys import stdin
input=stdin.readline
#1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, ...
data=[1,1,1,2,2]
#1+2=3 1+3=4
#1+4=5 2+5=7
#2+7=9 3+9=12
#4+12=16 ...
for i in range(100): data.append(data[i]+data[i+4])
for _ in range(int(input())):
    n=int(input())
    print(data[n-1])