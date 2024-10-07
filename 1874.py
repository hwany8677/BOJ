#pop연산이 중요해짐
#연산이 남았는데 스택이 빌 시 -> NO
from sys import stdin
input=stdin.readline
n=int(input())
order=[]
for _ in range(n): order.append(int(input()))
length=0
to_add=1
stack=[]
instructions=[]
i=0 #i=order
while(i<n):
    stack.append(to_add)
    instructions.append('+')
    length+=1
    to_add+=1
    if stack[length-1]>=order[i]:
        for j in range(length-1,-1,-1):
            if stack[j]==order[i]:
                stack.pop()
                instructions.append('-')
                length-=1
                i+=1
                break
            else:
                stack.pop()
                instructions.append('-')
                length-=1
for inst in instructions: print(inst)
