input=open(0).readline
order=[]
guess=[]
n=int(input())
for _ in range(n):
    buf=list(map(int,input().split()))
    order.append((buf[0]-1,buf[1]-1))
    guess.append(buf[2]-1)
mx=0
for i in range(3):
    count=0
    shell_pos=[j==i for j in range(3)]
    for j in range(n): #guess를 검증
        od=order[j]
        shell_pos[od[0]],shell_pos[od[1]]=shell_pos[od[1]],shell_pos[od[0]]
        if shell_pos[guess[j]]: count+=1
        if count>mx: mx=count
print(mx)
