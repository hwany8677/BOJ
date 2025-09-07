#pop연산이 중요해짐
#연산이 남았는데 스택이 빌 시 -> NO
#2025년 9월 8일 재작성
from sys import stdin
input=stdin.readline
n=int(input())
order=[]
for _ in range(n): order.append(int(input()))
length=1
to_add=2
stack=[1]
instructions=["+"]
i=0 #i=order
while(i<n):
    #push()하기 전, 윗부분이 같을 때 pop(), 아니면 push()
    #윗부분이 이미 원하는 수를 뛰어넘었으면 그 즉시 NO를 출력하고 종료.
    # print(f"Order: {order[i]}")
    # print(f"Stack: {stack}")
    # print(f"Last inst.: {instructions[len(instructions)-1]}")
    if length==0:
        stack.append(to_add)
        instructions.append("+")
        to_add+=1
        length+=1
    elif stack[length-1]>order[i]:
        print("NO")
        exit(0)
    elif stack[length-1]==order[i]:
        instructions.append("-")
        stack.pop()
        length-=1
        i+=1
    else:
        stack.append(to_add)
        instructions.append("+")
        to_add+=1
        length+=1
for inst in instructions: print(inst)