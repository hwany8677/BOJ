#Custom sorting
#
n=int(input())
b=list(map(int,input().split()))
b.sort()
b3,b2=[],[]
for element in b: 
    if element%3==0: b3.append(element)
    elif element%2==0: b2.append(element)
b3.reverse()
print(*b3,'',end='')
print(*b2)
