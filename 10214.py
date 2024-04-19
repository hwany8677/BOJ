t=int(input())
for i in range(0,t): 
    y,k=0,0
    for j in range(0,9):
        a,b=map(int,input().split())
        y+=a
        k+=b
    print("Yonsei" if y>k else "Korea" if y<k else "Draw")