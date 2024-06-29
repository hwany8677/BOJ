#'중간에 나갈 수도 있음'을 염두해둬야함
n=int(input())
line=list(map(int,input().split()))
#1을 먼저 보내기
toPass=1
queue=[]
line.reverse()
while(len(line)):
    # print(f"toPass: {toPass}")
    if len(queue):
        if toPass==queue[len(queue)-1]:
            queue.pop()
            toPass+=1
            continue
    if toPass==line[len(line)-1]:
        line.pop()
        toPass+=1
        continue
    queue.append(line[len(line)-1])
    line.pop()
for i in range(1,len(queue)):
    if queue[i-1]<queue[i]: 
        print("Sad")
        exit(0)
print("Nice")