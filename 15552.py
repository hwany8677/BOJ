from sys import stdin,stdout
for _ in range(int(stdin.readline())):
    a,b=map(int,stdin.readline().split())
    stdout.write(str(a+b))
    stdout.write('\n')