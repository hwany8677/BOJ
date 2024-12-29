#Magnus 필밴 = 승리
#Worst case = 무조건 패배
#--> (x-1)개의 라운드에서는 패배가 확정
input=open(0).readline
for _ in range(int(input())):
    x=int(input())
    print(2*x-1)
