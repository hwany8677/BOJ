#More Python-y
#'돌아는 간다'
n=int(input())+1
for i in range(1,n-1):
    print(" "*(n-i-1),end='')
    print("*"*(2*i-1))
for i in range(n-1,0,-1):
    print(" "*(n-i-1),end='')
    print("*"*(2*i-1))